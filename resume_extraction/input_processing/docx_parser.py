import docx

def extract_text_from_docx(file_path):

    doc = docx.Document(file_path)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)