import re

def extract_experience(text):

    experience_years = ""

    matches = re.findall(r'(\d+)\+?\s+years', text.lower())

    if matches:
        experience_years = matches[0]

    return experience_years