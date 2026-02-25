from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(text):
    return model.encode([text])

def calculate_similarity(text1, text2):
    emb1 = embed(text1)
    emb2 = embed(text2)
    score = cosine_similarity(emb1, emb2)[0][0]

    # Convert numpy float32 -> Python float
    return round(float(score) * 100, 2)

def section_based_score(resume_sections, jd_text):
    scores = {}

    for section, content in resume_sections.items():
        if content.strip():
            score = calculate_similarity(content, jd_text)
            scores[section] = float(score)  # ensure python float
        else:
            scores[section] = 0.0

    return scores