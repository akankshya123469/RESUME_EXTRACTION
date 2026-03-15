import fitz

def extract_text_from_pdf(pdf_path):
    """
    Extract text from text-based PDFs
    """

    text = ""

    try:
        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text()

    except Exception as e:
        print("PDF parsing error:", e)

    return text