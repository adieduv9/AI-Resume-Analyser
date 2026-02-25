import streamlit as st

def show():
    st.title("📊 Hiring Analytics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Match Score", "78.5%")

    with col2:
        st.metric("Average Resume Quality", "85.2%")

    with col3:
        st.metric("Total Resumes Processed", "42")

    st.markdown("---")
    st.info("Advanced analytics module coming soon.")