import re

def clean_text(text):
    """
    Clean resume text before entity extraction
    """

    if not text:
        return ""

    # remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # remove bullets and special characters
    text = re.sub(r'[•|▪]', ' ', text)

    # normalize new lines
    text = re.sub(r'\n+', '\n', text)

    return text.strip()