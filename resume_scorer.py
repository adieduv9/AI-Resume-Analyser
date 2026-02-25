import re

ACTION_VERBS = [
    "developed", "managed", "led", "designed",
    "built", "implemented", "created",
    "improved", "optimized"
]

def resume_quality_score(text):
    score = 0

    if 300 < len(text) < 3000:
        score += 20

    if re.search(r'\b[\w.-]+?@\w+?\.\w+?\b', text):
        score += 20

    if "-" in text or "•" in text:
        score += 20

    verb_count = sum(1 for verb in ACTION_VERBS if verb in text.lower())
    score += min(verb_count * 5, 20)

    if "experience" in text.lower():
        score += 10
    if "education" in text.lower():
        score += 10

    return min(score, 100)

def missing_keywords(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    missing = jd_words - resume_words
    return list(missing)[:20]