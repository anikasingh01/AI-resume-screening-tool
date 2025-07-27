import spacy
import PyPDF2

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def parse_resume(text):
    doc = nlp(text)
    return {
        "text": text,
        "skills": [ent.text for ent in doc.ents if ent.label_ in ["SKILL", "ORG"]],
        "experience": [ent.text for ent in doc.ents if ent.label_ == "DATE"],
        "education": [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    }
