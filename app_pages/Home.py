import streamlit as st
from enhanced_parser import parse_resume
from semantic_matcher import calculate_match_score, find_missing_keywords

def show():
    st.title("AI Resume Analyzer - Dynamic Matching")

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
    job_description = st.text_area("Paste Job Description Here")

    if uploaded_file and job_description:

        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        parsed = parse_resume("temp_resume.pdf")

        resume_text = parsed["raw_text"]

        st.subheader("Extracted Information")
        st.write("Name:", parsed["name"])
        st.write("Email:", parsed["email"])
        st.write("Skills:", parsed["skills"])

        score = calculate_match_score(resume_text, job_description)

        st.subheader("Match Score")
        st.success(f"{score}% Match with Job Description")

        missing_keywords = find_missing_keywords(resume_text, job_description)

        st.subheader("Missing Keywords")
        st.write(missing_keywords)