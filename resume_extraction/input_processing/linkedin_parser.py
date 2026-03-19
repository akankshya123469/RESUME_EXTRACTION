import requests
from bs4 import BeautifulSoup

def extract_linkedin_data(url):

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text()

        return text

    except:
        return ""