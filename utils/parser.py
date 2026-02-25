import re
import spacy

import PyPDF2

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Load small English model
nlp = spacy.load("en_core_web_sm")


def extract_name(text):
    """
    Extract name using multiple strategies:
    1. spaCy NER (PERSON)
    2. First 5 lines heuristic
    3. Capitalized line pattern
    """

    if not text or len(text.strip()) == 0:
        return "Not Found"

    # ----------------------------
    # 1️⃣ Try spaCy NER
    # ----------------------------
    doc = nlp(text[:1000])  # first part is enough

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text.strip()
            if len(name.split()) >= 2:
                return name

    # ----------------------------
    # 2️⃣ Try first 5 lines heuristic
    # ----------------------------
    lines = text.strip().split("\n")[:5]

    for line in lines:
        clean = line.strip()

        # Remove extra spaces
        clean = re.sub(r"\s+", " ", clean)

        # If line looks like a name
        if (
            2 <= len(clean.split()) <= 4
            and clean.replace(" ", "").isalpha()
            and not any(keyword in clean.lower() for keyword in ["engineer", "developer", "manager", "email", "phone"])
        ):
            return clean

    # ----------------------------
    # 3️⃣ Fallback: Capitalized pattern
    # ----------------------------
    pattern = r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+){1,2}\b"
    matches = re.findall(pattern, text)

    if matches:
        return matches[0]

    return "Not Found"