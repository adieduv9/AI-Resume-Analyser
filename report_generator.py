from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os

def generate_report(filename, data):
    os.makedirs("reports", exist_ok=True)

    filepath = os.path.join("reports", filename)
    doc = SimpleDocTemplate(filepath)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AI Resume Analysis Report", styles["Heading1"]))
    elements.append(Spacer(1, 0.5 * inch))

    for key, value in data.items():
        elements.append(Paragraph(f"<b>{key}:</b> {value}", styles["Normal"]))
        elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)