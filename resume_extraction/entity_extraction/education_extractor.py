import re

def extract_education(text):

    education = []

    patterns = [
        r"B\.?Tech.*",
        r"Bachelor.*",
        r"Master.*",
        r"Secondary.*",
        r"Higher Secondary.*"
    ]

    lines = text.split("\n")

    for line in lines:

        for pattern in patterns:

            if re.search(pattern, line, re.IGNORECASE):

                education.append(line.strip())

    return list(set(education))