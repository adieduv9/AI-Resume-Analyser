import streamlit as st
from streamlit_echarts import st_echarts
from utils.parser import extract_text_from_pdf
from utils.semantic_matcher import compute_match_score
import base64
import time
import random


def show():

    st.title("🧑‍💼 Candidate Resume Analysis")
    st.markdown("Upload your resume and get an AI-powered evaluation.")

    col_upload, col_preview = st.columns([2, 1])

    with col_upload:
        uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if uploaded_file:

        if st.button("🚀 Analyze Resume"):

            # Simulate processing delay
            with st.spinner("Analyzing resume..."):
                time.sleep(2)

            # 🔥 Replace this with your real scoring logic
            score = round(random.uniform(65, 92), 1)
            quality = round(random.uniform(70, 95), 1)

            skills_score = round(random.uniform(60, 90), 1)
            experience_score = round(random.uniform(65, 95), 1)
            education_score = round(random.uniform(70, 98), 1)

            st.markdown("## 🎯 Overall Match Score")

            # 🔥 Circular Gauge
            option = {
                "series": [
                    {
                        "type": "gauge",
                        "progress": {"show": True},
                        "detail": {"valueAnimation": True, "formatter": "{value}%"},
                        "data": [{"value": score}],
                        "min": 0,
                        "max": 100,
                    }
                ]
            }

            st_echarts(option, height="350px")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Match Score", f"{score}%")

            with col2:
                st.metric("Resume Quality", f"{quality}%")

            st.markdown("---")

            # 🔥 Section Breakdown Radar Chart
            st.markdown("## 📊 Section Breakdown")

            radar_option = {
                "tooltip": {},
                "radar": {
                    "indicator": [
                        {"name": "Skills", "max": 100},
                        {"name": "Experience", "max": 100},
                        {"name": "Education", "max": 100},
                    ]
                },
                "series": [
                    {
                        "type": "radar",
                        "data": [
                            {
                                "value": [
                                    skills_score,
                                    experience_score,
                                    education_score,
                                ],
                                "name": "Resume Analysis",
                            }
                        ],
                    }
                ],
            }

            st_echarts(radar_option, height="400px")

            st.markdown("---")

            # 🔥 AI Suggestions Section
            st.markdown("## 🤖 AI Improvement Suggestions")

            suggestions = []

            if skills_score < 75:
                suggestions.append("Add more role-specific technical keywords.")

            if experience_score < 75:
                suggestions.append("Quantify achievements with measurable impact (%, revenue, growth).")

            if education_score < 75:
                suggestions.append("Highlight relevant certifications or academic distinctions.")

            if not suggestions:
                suggestions.append("Your resume is well-optimized for ATS systems.")

            for s in suggestions:
                st.info(s)

            # 🔥 Resume Preview
            with col_preview:
                st.markdown("### 📄 Resume Preview")
                base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")
                pdf_display = f"""
                <iframe src="data:application/pdf;base64,{base64_pdf}" 
                width="100%" height="500" type="application/pdf"></iframe>
                """
                st.markdown(pdf_display, unsafe_allow_html=True)