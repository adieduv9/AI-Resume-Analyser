import streamlit as st

def inject_styles():
    st.markdown("""
    <style>
        /* App background */
        .stApp {
            background-color: #0f172a;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #111827;
        }

        /* Headings */
        h1, h2, h3, h4 {
            color: #f8fafc;
            font-weight: 600;
        }

        /* Paragraph */
        p {
            color: #cbd5e1;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            color: white;
            border-radius: 10px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
        }

        .stButton>button:hover {
            opacity: 0.85;
        }

        /* Metric cards */
        .metric-card {
            background-color: #1e293b;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 8px 24px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }

        /* Dataframe */
        .stDataFrame {
            border-radius: 10px;
        }

        /* Progress bar */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
        }
                
        .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
}

        .stMetric {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 12px;
}
    </style>
    """, unsafe_allow_html=True)