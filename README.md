# AI-powered-Resume-Screening-and-Ranking-System
An intelligent AI-based Resume Screening and Ranking System that automatically evaluates resumes against job descriptions, helping recruiters quickly identify top candidates.
<br>

📌 Features
✅ AI-driven Resume Ranking – Uses TF-IDF & Cosine Similarity to rank resumes based on job descriptions.<br>
✅ PDF Resume Parsing – Extracts text from resumes using pdfplumber.<br>
✅ Database Storage – Stores and retrieves resumes using SQLite.<br>
✅ Resume Upload & Management – Supports multiple resume uploads and stores them in a structured dataset.<br>
✅ User-Friendly Web Interface – Built using Streamlit for an interactive experience.<br>
✅ Download Best Matches – Allows recruiters to download top-ranked resumes easily.<br>


⚙️ Tech Stack<br>
Frontend: Streamlit<br>
Backend: Python <br>
Database: SQLite <br>
Machine Learning: Scikit-learn (TF-IDF, Cosine Similarity)<br>
File Processing: pdfplumber<br>


🚀 Installation & Setup<br>
1️⃣ Clone the Repository<br>
bash<br>
Copy<br>
Edit<br>
git clone https://github.com/vishwa-prajapati/AI-powered-Resume-Screening.git<br>
cd AI-powered-Resume-Screening<br>

2️⃣ Install Dependencies<br>
bash<br>
Copy<br>
Edit<br>
pip install -r requirements.txt<br>

3️⃣ Run the Application<br>
bash<br>
Copy<br>
Edit<br>
streamlit run app.py<br>
Now, open http://localhost:8501/ in your browser to use the application.<br>

📂 Project Structure<br>
bash<br>
Copy<br>
Edit<br>
AI-powered-Resume-Screening/
│── Resume Dataset/         # Uploaded resume files
│── src/                    # Source code
│── app.py                  # Streamlit app
│── requirements.txt         # Dependencies
│── README.md               # Project documentation
│── LICENSE                 # Open-source license
