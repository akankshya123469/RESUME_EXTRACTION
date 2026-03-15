import spacy

# load pretrained NLP model
nlp = spacy.load("en_core_web_sm")


import spacy

nlp = spacy.load("en_core_web_sm")

def extract_name(text):

    first_lines = text.split("\n")[0:5]
    header_text = " ".join(first_lines)

    doc = nlp(header_text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":

            name = ent.text

            name = name.replace("Phone","").replace("Email","").strip()

            return name

    return ""

def extract_companies(text):
    """
    Extract company names using ORG entities
    """

    doc = nlp(text)

    companies = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            companies.append(ent.text)

    return list(set(companies))