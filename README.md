🚀 AI Resume Analyzer

An AI-powered web app that analyzes a resume against a job description and provides a match score, skill gaps, and improvement suggestions.

🌐 Live Demo

👉 https://resume-analyzer-ai-c7p3ifb9ger8fd4xo9exuq.streamlit.app/

📌 Features
📊 Match Score using NLP (TF-IDF + Cosine Similarity)
🎯 Skill Match Percentage
⚠️ Missing Skills Detection
🔍 Keyword Highlighting
📄 Downloadable PDF Report
🌙 Dark Mode UI

🛠️ Tech Stack
Python
Streamlit
Scikit-learn
PyPDF2
ReportLab
NumPy

📂 Project Structure
resume-analyzer-ai/
│
├── app.py
├── requirements.txt
├── utils/
│   ├── parser.py
│   ├── analyzer.py
│
├── screenshots/
│
└── .streamlit/
    └── config.toml
▶️ How to Run Locally
1. Clone the Repository
git clone https://github.com/your-username/resume-analyzer-ai.git
cd resume-analyzer-ai
2. Create Virtual Environment
python -m venv venv

Activate:
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the App
streamlit run app.py
📖 How It Works
Upload a resume (PDF)
Paste a job description
System:
Extracts text from resume
Calculates similarity using NLP
Identifies skills from both inputs
Computes match score
Highlights missing keywords
Displays results + allows PDF download

🧠 Key Concepts Used
TF-IDF Vectorization
Cosine Similarity
Skill-based Matching
Text Processing

📌 Use Case
Helps students and job seekers:
Improve resumes
Identify missing skills
Prepare for job applications

🚀 Future Improvements
Advanced NLP using spaCy
Multiple resume comparison
AI-based suggestions
Resume ranking system

👩‍💻 Author
Maddhurika B
