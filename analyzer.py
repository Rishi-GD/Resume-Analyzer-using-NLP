# Resume Analyzer using NLP

import re
import docx2txt
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Extract text from resume
def extract_text_from_resume(file_path):
    return docx2txt.process(file_path)

# Extract skills using simple keyword matching
def extract_skills(text, skill_keywords):
    skills = []
    text_lower = text.lower()
    for skill in skill_keywords:
        if skill.lower() in text_lower:
            skills.append(skill)
    return list(set(skills))

# Main analyzer function
def analyze_resume(resume_path):
    text = extract_text_from_resume(resume_path)
    doc = nlp(text)
    skill_keywords = ['python', 'excel', 'machine learning', 'data analysis', 'project management',
                      'communication', 'sql', 'java', 'deep learning', 'nlp']
    skills_found = extract_skills(text, skill_keywords)
    return {
        'Name': doc.ents[0].text if doc.ents else 'N/A',
        'Skills': skills_found,
        'Summary': text[:300] + '...'
    }

# Example usage
# print(analyze_resume("sample_resume.docx"))
