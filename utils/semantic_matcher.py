from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import streamlit as st

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(text1, text2):
    model = load_model()
    emb1 = model.encode([text1])
    emb2 = model.encode([text2])
    similarity = cosine_similarity(emb1, emb2)[0][0]
    return float(similarity)

def compute_match_score(resume_text, job_description):
    similarity = compute_similarity(resume_text, job_description)
    return round(similarity * 100, 2)