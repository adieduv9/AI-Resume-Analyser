import streamlit as st
from styles import inject_styles
from app_pages import home, candidate, recruiter, analytics

st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="📄",
    layout="wide"
)

inject_styles()

st.sidebar.title("📄 AI Resume Analyzer Pro")
st.sidebar.markdown("AI-Powered Resume Intelligence Platform")

mode = st.sidebar.radio(
    "Navigation",
    ["Home", "Candidate", "Recruiter", "Analytics"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚡ Features")
st.sidebar.markdown("✔ Semantic Matching")
st.sidebar.markdown("✔ Skill Extraction")
st.sidebar.markdown("✔ Multi-Resume Ranking")

if mode == "Home":
    home.show()
elif mode == "Candidate":
    candidate.show()
elif mode == "Recruiter":
    recruiter.show()
elif mode == "Analytics":
    analytics.show()