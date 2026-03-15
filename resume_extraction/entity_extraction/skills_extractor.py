import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):

    doc = nlp(text)

    skills = []

    for token in doc:

        if token.pos_ == "PROPN" or token.pos_ == "NOUN":

            word = token.text.lower()

            if len(word) > 2 and len(word) < 20:
                skills.append(word)

    skills = list(set(skills))

    return skills[:25]