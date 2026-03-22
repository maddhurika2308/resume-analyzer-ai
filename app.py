import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.analyzer import calculate_similarity, extract_skills, get_missing_skills

# PDF generation
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io

# ------------------- CONFIG -------------------
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# ------------------- FUNCTIONS -------------------

def highlight_keywords(text, keywords):
    for word in keywords:
        text = text.replace(word, f"**:red[{word}]**")
    return text

def generate_pdf(score, match_percent, resume_skills, job_skills, missing_skills):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph(f"Match Score: {score}%", styles["Normal"]))
    content.append(Paragraph(f"Skill Match: {match_percent}%", styles["Normal"]))
    content.append(Paragraph(f"Resume Skills: {resume_skills}", styles["Normal"]))
    content.append(Paragraph(f"Job Skills: {job_skills}", styles["Normal"]))
    content.append(Paragraph(f"Missing Skills: {missing_skills}", styles["Normal"]))

    doc.build(content)

    buffer.seek(0)
    return buffer

# ------------------- UI -------------------

st.title("🚀 AI Resume Analyzer")
st.caption("AI-powered resume analysis with skill gap detection")

st.markdown("Upload your resume and compare it with a job description.")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("📝 Paste Job Description")

# ------------------- MAIN LOGIC -------------------

if uploaded_file and job_desc:
    resume_text = extract_text_from_pdf(uploaded_file)

    # Text similarity
    text_score = calculate_similarity(resume_text, job_desc)

    # Skill extraction
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    matched_skills = set(resume_skills) & set(job_skills)
    missing_skills = get_missing_skills(resume_skills, job_skills)
    if job_skills:
        skill_score = (len(matched_skills) / len(job_skills)) * 100
        match_percent = round(skill_score, 2)
    else:
        skill_score = 0
        match_percent = 0

    # Final score (weighted)
    score = round((0.3 * text_score) + (0.7 * skill_score), 2)

    st.markdown("---")

    # ------------------- MATCH SCORE -------------------
    st.subheader("📊 Match Score")

    if score > 75:
        st.success(f"{score}% - Strong Match ✅")
    elif score > 50:
        st.warning(f"{score}% - Moderate Match ⚠️")
    else:
        st.error(f"{score}% - Weak Match ❌")

    st.progress(score / 100)

    st.markdown("---")

    # ------------------- SKILL MATCH -------------------
    st.subheader("🎯 Skill Match")

    st.write(f"{match_percent}% skills matched")
    st.progress(match_percent / 100)

    st.subheader("✅ Matched Skills")
    st.write(list(matched_skills))

    st.markdown("---")

    # ------------------- SKILLS DISPLAY -------------------
    st.subheader("💡 Your Skills")
    st.write(resume_skills if resume_skills else "No skills detected")

    st.subheader("📌 Required Skills (from Job)")
    st.write(job_skills if job_skills else "No skills detected")

    st.markdown("---")

    # ------------------- MISSING SKILLS -------------------
    st.subheader("⚠️ Missing Skills")

    

    if missing_skills:
        st.write(missing_skills)
    else:
        st.success("You match all required skills 🎯")

    # ------------------- SUGGESTIONS -------------------
    if missing_skills:
        st.markdown("---")
        st.subheader("🚀 Suggestions")
        st.write("To improve your resume, consider adding:")
        st.write(missing_skills)

    # ------------------- KEYWORD HIGHLIGHT -------------------
    st.markdown("---")
    st.subheader("🔍 Keyword Analysis (Missing in Resume)")

    if missing_skills:
        highlighted_text = highlight_keywords(job_desc, missing_skills)
        st.markdown(highlighted_text)
    else:
        st.success("No missing keywords 🎯")

    # ------------------- DOWNLOAD REPORT -------------------
    st.markdown("---")
    st.subheader("📄 Download Report")

    pdf_file = generate_pdf(score, match_percent, resume_skills, job_skills, missing_skills)

    st.download_button(
        label="Download PDF Report",
        data=pdf_file,
        file_name="resume_analysis.pdf",
        mime="application/pdf"
    )

# ------------------- FOOTER -------------------
st.markdown("---")
st.caption("Built using Python & Streamlit")