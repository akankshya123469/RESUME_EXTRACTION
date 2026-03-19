class ResumeExtractor:

    def __init__(self):
        pass

    def extract_text(self, input_data):

        from input_processing.pdf_parser import extract_text_from_pdf
        from input_processing.docx_parser import extract_text_from_docx
        from input_processing.ocr_engine import extract_text_from_scanned_pdf
        from input_processing.linkedin_parser import extract_linkedin_data


        text = ""

        # PDF
        if isinstance(input_data, str) and input_data.endswith(".pdf"):

            text = extract_text_from_pdf(input_data)

            # If text too small → scanned PDF
            if len(text.strip()) < 50:
                text = extract_text_from_scanned_pdf(input_data)

        # DOCX
        elif isinstance(input_data, str) and input_data.endswith(".docx"):

            text = extract_text_from_docx(input_data)

        # LinkedIn URL
        elif isinstance(input_data, str) and input_data.startswith("http"):

            text = extract_linkedin_data(input_data)

        # Direct text
        else:
            text = input_data

        return text

    def process(self, input_data):

        from utils.text_cleaner import clean_text
        from entity_extraction.skills_extractor import extract_skills
        from entity_extraction.education_extractor import extract_education
        from entity_extraction.projects_extractor import extract_projects
        from entity_extraction.experience_extractor import extract_experience
        from entity_extraction.ner_model import extract_name, extract_companies
        from output.json_formatter import format_output

        # Step 1: Extract text
        text = self.extract_text(input_data)

        # Step 2: Clean text
        text = clean_text(text)

        # Step 3: Entity extraction
        name = extract_name(text)
        companies = extract_companies(text)
        skills = extract_skills(text)
        education = extract_education(text)
        projects = extract_projects(text)
        experience = extract_experience(text)

        # Step 4: Format output
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

    extractor = ResumeExtractor()

    # Test input (change as needed)
    file_path = "sample_resumes/resume1.pdf"

    result = extractor.process(file_path)

    print(result)