def read_pdf(file_path):
    from PyPDF2 import PdfReader

    text = ""
    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()