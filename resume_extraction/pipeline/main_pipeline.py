import os

from input_processing.pdf_parser import extract_text_from_pdf
from input_processing.docx_parser import extract_text_from_docx
from input_processing.ocr_engine import extract_text_from_scanned_pdf

from utils.text_cleaner import clean_text

from entity_extraction.skills_extractor import extract_skills
from entity_extraction.education_extractor import extract_education
from entity_extraction.projects_extractor import extract_projects
from entity_extraction.experience_extractor import extract_experience
from entity_extraction.ner_model import extract_name, extract_companies

from output.json_formatter import format_output


def process_resume(input_data):

    text = ""

    # Detect input type
    if isinstance(input_data, str) and input_data.endswith(".pdf"):

        text = extract_text_from_pdf(input_data)

        # If empty → scanned PDF
        if len(text.strip()) < 50:
            text = extract_text_from_scanned_pdf(input_data)

    elif isinstance(input_data, str) and input_data.endswith(".docx"):

        text = extract_text_from_docx(input_data)

    else:
        # Direct text input
        text = input_data

    # Clean text
    text = clean_text(text)

    # Extract entities
    name = extract_name(text)
    companies = extract_companies(text)
    skills = extract_skills(text)
    education = extract_education(text)
    projects = extract_projects(text)
    experience = extract_experience(text)

    # Format JSON
    result = format_output(
        name,
        skills,
        education,
        companies,
        experience,
        projects
    )

    return result


if __name__ == "__main__":

    file_path = "sample_resumes/resume1.pdf"

    result = process_resume(file_path)

    print(result)