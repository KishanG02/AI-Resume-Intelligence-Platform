from pypdf import PdfReader
from docx import Document


def parse_pdf(uploaded_file):
    text = ""

    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def parse_docx(uploaded_file):
    doc = Document(uploaded_file)

    text = "\n".join(
        [paragraph.text for paragraph in doc.paragraphs]
    )

    return text