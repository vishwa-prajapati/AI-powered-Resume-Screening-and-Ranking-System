# AI-powered-Resume-Screening-and-Ranking-System
An intelligent AI-based Resume Screening and Ranking System that automatically evaluates resumes against job descriptions, helping recruiters quickly identify top candidates.
<br>

📌 Features<br>
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
bash>Copy>Edit <br>
```bash
git clone https://github.com/vishwa-prajapati/AI-powered-Resume-Screening.git
cd AI-powered-Resume-Screening```

2️⃣ Install Dependencies<br>
bash>Copy>Edit 
```bash
pip install -r requirements.txt```

3️⃣ Run the Application<br>
bash>Copy>Edit <br>
```bash
streamlit run app.py
Now, open http://localhost:8501/ in your browser to use the application.```

📂 Project Structure<br>
bash>Copy>Edit
AI-powered-Resume-Screening/
│── Resume Dataset/         # Uploaded resume files <br>
│── src/                    # Source code <br>
│── app.py                  # Streamlit app <br>
│── requirements.txt         # Dependencies <br>
│── README.md               # Project documentation <br>
│── LICENSE                 # Open-source license <br>
