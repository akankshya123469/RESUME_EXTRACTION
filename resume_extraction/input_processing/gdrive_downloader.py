import gdown

def download_from_gdrive(url):

    output = "temp_resume.pdf"

    gdown.download(url, output, quiet=False)

    return output