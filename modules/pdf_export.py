from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_pdf(text, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    for line in text.split("\n"):

        content.append(
            Paragraph(line, styles["Normal"])
        )

        content.append(
            Spacer(1, 6)
        )

    doc.build(content)

    return filename