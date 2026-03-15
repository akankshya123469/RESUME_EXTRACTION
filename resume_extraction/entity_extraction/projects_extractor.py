import re

def extract_projects(text):

    projects = []

    pattern = r"projects(.*?)(education|skills|certifications|additional)"

    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if match:

        section = match.group(1)

        lines = section.split("\n")

        for line in lines:

            if len(line) > 10:
                projects.append(line.strip())

    return projects[:5]