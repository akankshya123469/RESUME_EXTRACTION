import fitz
import pytesseract
from PIL import Image


def extract_text_from_scanned_pdf(file_path):

    doc = fitz.open(file_path)

    text = ""

    for page in doc:

        pix = page.get_pixmap()

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        page_text = pytesseract.image_to_string(img)

        text += page_text

    return text