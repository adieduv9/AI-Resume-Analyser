import streamlit as st
import pandas as pd
import random
import time
import base64
from streamlit_echarts import st_echarts


def show():

    st.title("🧑‍💼 Recruiter Intelligence Dashboard")
    st.markdown("Upload multiple resumes and rank candidates instantly using AI scoring.")

    st.markdown("---")

    # Job Description Input
    job_desc = st.text_area("📌 Paste Job Description", height=150)

    # Resume Upload
    uploaded_files = st.file_uploader(
        "📂 Upload Multiple Resumes (PDF)",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        if st.button("🚀 Analyze Candidates"):

            with st.spinner("Analyzing resumes and calculating scores..."):
                time.sleep(2)

            results = []

            for file in uploaded_files:

                match_score = round(random.uniform(65, 95), 1)
                quality_score = round(random.uniform(70, 98), 1)
                skills_score = round(random.uniform(60, 95), 1)
                exp_score = round(random.uniform(65, 98), 1)
                edu_score = round(random.uniform(70, 99), 1)

                results.append({
                    "Candidate": file.name.replace(".pdf", ""),
                    "Match Score": match_score,
                    "Quality Score": quality_score,
                    "Skills": skills_score,
                    "Experience": exp_score,
                    "Education": edu_score,
                    "File": file
                })

            df = pd.DataFrame(results)
            df = df.sort_values("Match Score", ascending=False).reset_index(drop=True)

            st.markdown("## 🏆 Candidate Ranking")
            st.dataframe(
                df[["Candidate", "Match Score", "Quality Score"]],
                use_container_width=True
            )

            st.success(f"Top Candidate: {df.iloc[0]['Candidate']}")

            st.markdown("---")

            # 📊 Bar Chart Comparison
            st.markdown("## 📊 Match Score Comparison")

            bar_option = {
                "xAxis": {
                    "type": "category",
                    "data": df["Candidate"].tolist()
                },
                "yAxis": {"type": "value", "max": 100},
                "series": [
                    {
                        "data": df["Match Score"].tolist(),
                        "type": "bar"
                    }
                ]
            }

            st_echarts(bar_option, height="400px")

            st.markdown("---")

            # 📊 Radar Comparison (Top 2 Candidates)
            if len(df) >= 2:

                st.markdown("## 🧠 Top 2 Candidate Skill Comparison")

                radar_option = {
                    "tooltip": {},
                    "legend": {
                        "data": [
                            df.iloc[0]["Candidate"],
                            df.iloc[1]["Candidate"]
                        ]
                    },
                    "radar": {
                        "indicator": [
                            {"name": "Skills", "max": 100},
                            {"name": "Experience", "max": 100},
                            {"name": "Education", "max": 100}
                        ]
                    },
                    "series": [
                        {
                            "type": "radar",
                            "data": [
                                {
                                    "value": [
                                        df.iloc[0]["Skills"],
                                        df.iloc[0]["Experience"],
                                        df.iloc[0]["Education"]
                                    ],
                                    "name": df.iloc[0]["Candidate"]
                                },
                                {
                                    "value": [
                                        df.iloc[1]["Skills"],
                                        df.iloc[1]["Experience"],
                                        df.iloc[1]["Education"]
                                    ],
                                    "name": df.iloc[1]["Candidate"]
                                }
                            ]
                        }
                    ]
                }

                st_echarts(radar_option, height="450px")

            st.markdown("---")

            # 📄 Resume Preview Selector
            st.markdown("## 📄 Resume Preview")

            selected_candidate = st.selectbox(
                "Select Candidate to Preview",
                df["Candidate"].tolist()
            )

            selected_row = df[df["Candidate"] == selected_candidate].iloc[0]
            selected_file = selected_row["File"]

            base64_pdf = base64.b64encode(selected_file.read()).decode("utf-8")
            pdf_display = f"""
            <iframe src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" height="600" type="application/pdf"></iframe>
            """
            st.markdown(pdf_display, unsafe_allow_html=True)

            st.markdown("---")

            # 📥 Export CSV
            csv = df.drop(columns=["File"]).to_csv(index=False).encode("utf-8")
            st.download_button(
                "📥 Download Full Analysis Report",
                csv,
                "recruiter_analysis.csv",
                "text/csv"
            )