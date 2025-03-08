# AI-powered-Resume-Screening-and-Ranking-System
An intelligent AI-based Resume Screening and Ranking System that automatically evaluates resumes against job descriptions, helping recruiters quickly identify top candidates.

📌 Features
✅ AI-driven Resume Ranking – Uses TF-IDF & Cosine Similarity to rank resumes based on job descriptions.
✅ PDF Resume Parsing – Extracts text from resumes using pdfplumber.
✅ Database Storage – Stores and retrieves resumes using SQLite.
✅ Resume Upload & Management – Supports multiple resume uploads and stores them in a structured dataset.
✅ User-Friendly Web Interface – Built using Streamlit for an interactive experience.
✅ Download Best Matches – Allows recruiters to download top-ranked resumes easily.

⚙️ Tech Stack
Frontend: Streamlit
Backend: Python, Flask
Database: SQLite
Machine Learning: Scikit-learn (TF-IDF, Cosine Similarity)
File Processing: pdfplumber
🚀 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/AI-powered-Resume-Screening.git
cd AI-powered-Resume-Screening
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Application
bash
Copy
Edit
streamlit run app.py
Now, open http://localhost:8501/ in your browser to use the application.

📂 Project Structure
bash
Copy
Edit
AI-powered-Resume-Screening/
│── database/               # Stores resumes in SQLite database
│── Resume Dataset/         # Uploaded resume files
│── src/                    # Source code
│── app.py                  # Streamlit app
│── requirements.txt         # Dependencies
│── README.md               # Project documentation
│── LICENSE                 # Open-source license
