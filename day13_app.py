# =============================================================
# DAY 13 — Streamlit UI for AI Resume Analyzer
# Project: AI Resume Analyzer
# Run: streamlit run day13_app.py
# =============================================================

# STEP 0: Install dependencies (run once)
# pip install streamlit spacy scikit-learn pandas matplotlib pdfplumber
# python3 -m spacy download en_core_web_sm

import re
import spacy
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import fitz  # pymupdf
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ── Page config ───────────────────────────────────────────────
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ── Load spaCy ────────────────────────────────────────────────
@st.cache_resource
def load_nlp():
    return spacy.load("en_core_web_sm")

nlp = load_nlp()


# =============================================================
# SKILL DATABASE
# =============================================================

SKILLS_DB = sorted([
    "python", "java", "javascript", "c++", "typescript",
    "machine learning", "deep learning", "nlp", "data science",
    "scikit-learn", "tensorflow", "keras", "pytorch", "xgboost",
    "pandas", "numpy", "matplotlib", "seaborn", "sql", "mysql",
    "mongodb", "postgresql", "sqlite", "redis",
    "html", "css", "react", "node.js", "express.js", "django", "flask",
    "rest api", "rest apis", "tailwind css", "bootstrap", "graphql",
    "aws", "azure", "gcp", "docker", "kubernetes", "git", "linux",
    "tableau", "power bi", "postman", "figma", "firebase", "agile",
], key=len, reverse=True)


# =============================================================
# HELPER FUNCTIONS
# =============================================================

def extract_text_from_pdf(uploaded_file):
    text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text


def extract_skills(text):
    text_lower = text.lower()
    found = []
    for skill in SKILLS_DB:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found.append(skill)
    return sorted(set(found))


def extract_education(text):
    degree_re = re.compile(
        r"B\.?Tech|M\.?Tech|B\.?E|M\.?E|B\.?Sc|M\.?Sc"
        r"|Bachelor|Master|PhD|MBA|BCA|MCA|BBA",
        re.IGNORECASE
    )
    return [line.strip() for line in text.split("\n")
            if degree_re.search(line) and len(line.strip()) > 5]


def extract_experience_years(text):
    explicit = re.findall(
        r'(\d+)\s+year[s]?\s+of\s+experience', text, re.IGNORECASE)
    if explicit:
        return int(explicit[0])
    ranges = re.findall(r'(\d{4})\s*[–\-]\s*(\d{4})', text)
    return sum(int(e) - int(s) for s, e in ranges) if ranges else 0


def extract_contact(text):
    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', text)
    phones = re.findall(r'(?:\+91[\-\s]?)?[6-9]\d{9}', text)
    return (emails[0] if emails else "Not found",
            phones[0] if phones else "Not found")


def score_resume(resume_text, job_description):
    """Compute TF-IDF + skill match combined score."""
    # TF-IDF score
    vectorizer  = TfidfVectorizer(stop_words="english")
    tfidf       = vectorizer.fit_transform([job_description, resume_text])
    tfidf_score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100

    # Skill match score
    jd_skills     = set(extract_skills(job_description))
    resume_skills = set(extract_skills(resume_text))
    matched       = jd_skills & resume_skills
    missing       = jd_skills - resume_skills
    skill_score   = (len(matched) / len(jd_skills) * 100) if jd_skills else 0

    final_score = round((tfidf_score * 0.5) + (skill_score * 0.5), 1)

    grade = (
        "🟢 Excellent Match" if final_score >= 70 else
        "🟡 Good Match"      if final_score >= 50 else
        "🔴 Weak Match"
    )

    return {
        "final_score" : final_score,
        "tfidf_score" : round(tfidf_score, 1),
        "skill_score" : round(skill_score, 1),
        "matched"     : sorted(matched),
        "missing"     : sorted(missing),
        "grade"       : grade,
    }


# =============================================================
# STREAMLIT UI
# =============================================================

# ── Header ────────────────────────────────────────────────────
st.title("📄 AI Resume Analyzer")
st.markdown("Upload your resume and paste a job description to get your **match score, skill analysis, and recommendations.**")
st.divider()

# ── Layout: two columns ───────────────────────────────────────
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Upload Resume")
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF or paste text below)",
        type=["pdf"]
    )
    st.markdown("**Or paste resume text directly:**")
    resume_text_input = st.text_area(
        "Resume text",
        height=200,
        placeholder="Paste your resume text here..."
    )

with col2:
    st.subheader("📋 Job Description")
    job_desc_input = st.text_area(
        "Paste the job description here",
        height=280,
        placeholder="Paste the job description you want to match against..."
    )

st.divider()

# ── Analyze button ────────────────────────────────────────────
analyze = st.button("🔍 Analyze Resume", type="primary", use_container_width=True)

if analyze:
    # Get resume text
    resume_text = ""
    if uploaded_file:
        with st.spinner("Reading PDF..."):
            resume_text = extract_text_from_pdf(uploaded_file)
        st.success("✅ PDF loaded successfully!")
    elif resume_text_input.strip():
        resume_text = resume_text_input.strip()
    else:
        st.error("⚠️ Please upload a PDF or paste your resume text!")
        st.stop()

    if not job_desc_input.strip():
        st.error("⚠️ Please paste a job description!")
        st.stop()

    with st.spinner("Analyzing resume..."):

        # Extract info
        skills      = extract_skills(resume_text)
        education   = extract_education(resume_text)
        exp_years   = extract_experience_years(resume_text)
        email, phone = extract_contact(resume_text)
        scores      = score_resume(resume_text, job_desc_input)

    st.divider()

    # ── Score display ─────────────────────────────────────────
    st.subheader("🏆 Match Score")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Final Score",   f"{scores['final_score']}%")
    c2.metric("TF-IDF Score",  f"{scores['tfidf_score']}%")
    c3.metric("Skill Match",   f"{scores['skill_score']}%")
    c4.metric("Grade",          scores["grade"])

    # Score progress bar
    st.progress(int(scores["final_score"]))

    st.divider()

    # ── Two column results ────────────────────────────────────
    r1, r2 = st.columns(2)

    with r1:
        st.subheader("👤 Candidate Info")
        st.write(f"📧 **Email:** {email}")
        st.write(f"📱 **Phone:** {phone}")
        st.write(f"💼 **Experience:** {exp_years} year(s)")
        st.write(f"🎓 **Education:**")
        for e in education:
            st.write(f"  - {e}")

        st.subheader("🛠️ Skills Found")
        if skills:
            st.write(", ".join([f"`{s}`" for s in skills]))
        else:
            st.write("No skills detected")

    with r2:
        st.subheader("✅ Matched Skills")
        if scores["matched"]:
            for s in scores["matched"]:
                st.success(f"✔ {s}")
        else:
            st.write("No matching skills found")

        st.subheader("❌ Missing Skills")
        if scores["missing"]:
            for s in scores["missing"]:
                st.error(f"✘ {s}")
        else:
            st.write("🎉 You have all required skills!")

    st.divider()

    # ── Skill chart ───────────────────────────────────────────
    st.subheader("📊 Skill Match Chart")

    if scores["matched"] or scores["missing"]:
        fig, ax = plt.subplots(figsize=(8, 3))
        categories = ["Matched Skills", "Missing Skills"]
        values     = [len(scores["matched"]), len(scores["missing"])]
        colors     = ["#2ecc71", "#e74c3c"]
        bars = ax.barh(categories, values, color=colors, height=0.4)
        for bar, val in zip(bars, values):
            ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                    str(val), va="center", fontsize=12)
        ax.set_xlabel("Number of Skills")
        ax.set_title("Resume Skills vs Job Requirements")
        ax.set_xlim(0, max(values) + 2)
        plt.tight_layout()
        st.pyplot(fig)

    st.divider()

    # ── Recommendations ───────────────────────────────────────
    st.subheader("💡 Recommendations")

    if scores["final_score"] >= 70:
        st.success("🎉 Great match! Your resume is well suited for this job.")
        st.info("💡 Tip: Tailor your resume summary to mention the job title directly.")
    elif scores["final_score"] >= 50:
        st.warning("👍 Good match! A few improvements can make you a strong candidate.")
    else:
        st.error("📚 Your resume needs work for this specific role.")

    if scores["missing"]:
        st.markdown("**Skills to add or learn:**")
        for skill in scores["missing"]:
            st.markdown(f"- 📖 Learn **{skill}** → search on Coursera / YouTube / Udemy")

    # ── Download results ──────────────────────────────────────
    st.divider()
    st.subheader("💾 Download Results")

    result_df = pd.DataFrame([{
        "Final Score"    : scores["final_score"],
        "TF-IDF Score"   : scores["tfidf_score"],
        "Skill Score"    : scores["skill_score"],
        "Grade"          : scores["grade"],
        "Matched Skills" : ", ".join(scores["matched"]),
        "Missing Skills" : ", ".join(scores["missing"]),
        "Experience Yrs" : exp_years,
        "Education"      : " | ".join(education),
        "Email"          : email,
    }])

    csv = result_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Results as CSV",
        data=csv,
        file_name="resume_analysis_result.csv",
        mime="text/csv",
        use_container_width=True
    )

# ── Footer ────────────────────────────────────────────────────
st.divider()
st.markdown(
    "<center>Built with ❤️ by Jayaprakash | AI Resume Analyzer Project</center>",
    unsafe_allow_html=True
)
