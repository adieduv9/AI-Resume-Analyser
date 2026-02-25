import spacy
import re
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Not Found"

def extract_email(text):
    match = re.search(r'\b[\w.-]+?@\w+?\.\w+?\b', text)
    return match.group(0) if match else "Not Found"

def extract_sections(text):
    sections = {
        "skills": "",
        "experience": "",
        "education": ""
    }

    lines = text.split("\n")
    current_section = None

    for line in lines:
        l = line.lower()

        if "skill" in l:
            current_section = "skills"
        elif "experience" in l:
            current_section = "experience"
        elif "education" in l:
            current_section = "education"

        if current_section:
            sections[current_section] += line + " "

    return sections

def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    sections = extract_sections(text)

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "raw_text": text,
        "sections": sections
    }