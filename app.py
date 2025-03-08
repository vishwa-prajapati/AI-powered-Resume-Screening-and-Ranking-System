import streamlit as st
import os
import sqlite3
import pdfplumber
import numpy as np
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.markdown(
    """
    <style>
    .stApp {
        background-color: #13b0ab;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ✅ Ensure required folders exist
DB_FOLDER = "database"
RESUME_DATASET_FOLDER = "Resume Dataset"
DB_PATH = os.path.join(DB_FOLDER, "resumes.db")

for folder in [DB_FOLDER, RESUME_DATASET_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# ✅ Connect to the database
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

# ✅ Create resumes table (if not exists) without job_role
c.execute('''
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT UNIQUE, 
        file_path TEXT, 
        text TEXT, 
        upload_date TEXT
    )
''')
conn.commit()

# ✅ Function to extract text from PDFs
def extract_text_from_pdf(file):
    try:
        with pdfplumber.open(file) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages).strip()
        return text if text else None  # Return None if text is empty
    except Exception:
        return None  # Silently handle errors by returning None

# ✅ Function to rank resumes
def rank_resumes(job_description, resumes):
    try:
        documents = [job_description] + resumes
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform(documents).toarray()
        job_description_vector = vectors[0]
        resume_vectors = vectors[1:]
        similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
        return similarities
    except Exception:
        return [0] * len(resumes)

# ✅ Function to get all resumes from the database
def get_all_resumes():
    resumes = {}
    c.execute("SELECT name, text, file_path FROM resumes")
    db_resumes = c.fetchall()
    for name, text, file_path in db_resumes:
        resumes[name] = (text, file_path)
    return resumes

def clean_database():
    """Removes database entries for missing files."""
    c.execute("SELECT id, name, file_path FROM resumes")
    resumes = c.fetchall()
    
    deleted_count = 0
    for resume_id, name, file_path in resumes:
        if not os.path.exists(file_path):  # If file does not exist
            c.execute("DELETE FROM resumes WHERE id = ?", (resume_id,))
            conn.commit()
            deleted_count += 1

    if deleted_count > 0:
        st.success(f"🗑 Removed {deleted_count} missing resumes from database!")
    else:
        st.info("✅ All records are valid, no missing files found.")


# ✅ Streamlit UI
def main():
    st.title("🚀 AI Resume Matcher with Database & Resume Dataset")

    # Upload Resume Section
    st.subheader("📂 Upload Resumes")
    uploaded_files = st.file_uploader("Upload PDF Resumes", type=["pdf"], accept_multiple_files=True)

    uploaded_resume_texts = []
    uploaded_resume_names = []
    uploaded_resume_paths = []
    uploaded_resume_bytes = {}

    if uploaded_files:
        for uploaded_file in uploaded_files:
            resume_bytes = uploaded_file.getvalue()  # Read file content properly
            resume_text = extract_text_from_pdf(uploaded_file)
            resume_path = os.path.join(RESUME_DATASET_FOLDER, uploaded_file.name)

            # ✅ Save uploaded resume in dataset folder
            with open(resume_path, "wb") as f:
                f.write(resume_bytes)

            # ✅ Save details in database
            upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute(
                "INSERT INTO resumes (name, file_path, text, upload_date) VALUES (?, ?, ?, ?)", 
                (uploaded_file.name, resume_path, resume_text, upload_date)
            )
            conn.commit()

            uploaded_resume_texts.append(resume_text)
            uploaded_resume_names.append(uploaded_file.name)
            uploaded_resume_paths.append(resume_path)
            uploaded_resume_bytes[uploaded_file.name] = resume_bytes  # Store for downloading

        st.success(f"✅ {len(uploaded_files)} resumes uploaded & added to dataset!")

    # Job Description Input
    st.subheader("💼 Enter Job Description")
    job_description = st.text_area("Paste the job description here")

    if st.button("🔍 Find Best Matches"):
        all_resumes = get_all_resumes()

        # Combine uploaded resumes with existing dataset
        for i in range(len(uploaded_resume_names)):
            all_resumes[uploaded_resume_names[i]] = (uploaded_resume_texts[i], uploaded_resume_paths[i])

        if all_resumes:
            names = list(all_resumes.keys())
            resume_texts = [all_resumes[name][0] for name in names]
            file_paths = [all_resumes[name][1] for name in names]

            similarities = rank_resumes(job_description, resume_texts)
            sorted_indices = np.argsort(similarities)[::-1]

            top_matches = []
            seen_names = set()
            for idx in sorted_indices:
                if names[idx] not in seen_names:
                    seen_names.add(names[idx])
                    top_matches.append((names[idx], similarities[idx] * 100, file_paths[idx]))
                if len(top_matches) == 3:
                    break

            st.subheader("🏆 Top 3 Matching Resumes")
            for idx, (name, match, path) in enumerate(top_matches):
                if name in uploaded_resume_bytes:
                    file_bytes = uploaded_resume_bytes[name]
                else:
                    with open(path, "rb") as file:
                        file_bytes = file.read()

                st.download_button(
                    label=f"📥 Download {name} ({match:.2f}% match)",
                    data=file_bytes,
                    file_name=name,
                    mime="application/pdf",
                    key=f"download_{idx}"
                )

            # ✅ Show uploaded resume scores
            if uploaded_resume_names:
                st.subheader("📊 Uploaded Resume Scores")
                for i in range(len(uploaded_resume_names)):
                    score = similarities[names.index(uploaded_resume_names[i])] * 100
                    st.write(f"✅ {uploaded_resume_names[i]}: *{score:.2f}% match*")
        else:
            st.warning("⚠ No resumes found!")
            
if st.button("🗑 Clean Missing Resumes from Database"):
        clean_database()

if __name__ == "__main__":
    main()
