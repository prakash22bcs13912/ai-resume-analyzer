# 📄 AI Resume Analyzer

An end-to-end Machine Learning project that analyzes resumes, extracts skills, scores candidates against job descriptions, and recommends courses to fill skill gaps.

---

## 🚀 Live Demo

> Run locally using Streamlit (see instructions below)

---

## 📌 Project Overview

This project was built over 14 days as a complete ML pipeline:

| Day | Topic |
|-----|-------|
| Day 4 | Data preprocessing |
| Day 5 | Data cleaning |
| Day 6 | Feature extraction |
| Day 8 | Model building |
| Day 9 | Model evaluation |
| Day 10 | NLP skill extraction using spaCy |
| Day 11 | Resume scoring & job matching |
| Day 12 | Recommendation engine |
| Day 13 | Streamlit web app UI |

---

## ✨ Features

- 📤 Upload PDF resume or paste resume text
- 📋 Paste any job description
- 🏆 Get match score out of 100%
- ✅ See matched skills
- ❌ See missing skills
- 📚 Get course recommendations for missing skills
- 💡 Get personalized resume tips
- 📥 Download results as CSV

---

## 🛠️ Tech Stack

- **Python** — core language
- **spaCy** — NLP and named entity recognition
- **Scikit-learn** — TF-IDF vectorizer and cosine similarity
- **Pandas** — data processing
- **Matplotlib** — data visualization
- **Streamlit** — web app UI
- **pdfplumber** — PDF text extraction
- **Git & GitHub** — version control

---

## ⚙️ Installation

**Step 1 — Clone the repo:**
```bash
git clone https://github.com/prakash22bcs13912/ai-resume-analyzer
cd ai-resume-analyzer
```

**Step 2 — Install dependencies:**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**Step 3 — Run the app:**
```bash
streamlit run day13_app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📊 How It Works

```
Resume (PDF/Text)
       ↓
Text Extraction (pdfplumber)
       ↓
NLP Processing (spaCy)
       ↓
Skill Extraction (keyword matching)
       ↓
TF-IDF Scoring (cosine similarity)
       ↓
Match Score + Recommendations
```

---

## 📁 Project Structure

```
ai-resume-analyzer/
│
├── day10_nlp_skill_extraction.py   # NLP pipeline
├── day11_resume_scoring.py         # Scoring engine
├── day12_recommendations.py        # Recommendation engine
├── day13_app.py                    # Streamlit UI
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation
```

---

## 👨‍💻 Author

**Jayaprakash**
- GitHub: [@prakash22bcs13912](https://github.com/prakash22bcs13912)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
