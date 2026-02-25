import streamlit as st

def show():
    st.title("📄 AI Resume Analyzer Pro")

    st.markdown("""
    ### AI-Powered Resume Intelligence Platform
    
    Analyze resumes with semantic skill matching,
    recruiter ranking systems, and quality scoring.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
        <h3>🎯 Smart Matching</h3>
        <p>Advanced skill extraction & semantic scoring.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
        <h3>📊 Recruiter Dashboard</h3>
        <p>Rank multiple candidates instantly.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
        <h3>📈 Analytics</h3>
        <p>Data-driven hiring insights.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.success("Select a mode from the sidebar to begin.")