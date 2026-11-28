from pypdf import PdfReader
from io import BytesIO


def extract_text_from_pdf(pdf_bytes):

    try:
        # Convert uploaded bytes into a readable PDF
        pdf_file = BytesIO(pdf_bytes)

        reader = PdfReader(pdf_file)

        extracted_text = ""

        # Extract text from every page
        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

        # Handle empty PDF
        if not extracted_text.strip():
            return {
                "message": "No readable text found in the PDF.",
                "extracted_text": "",
                "total_pages": len(reader.pages),
                "character_count": 0
            }

        return {
            "message": "PDF text extracted successfully.",
            "extracted_text": extracted_text.strip(),
            "total_pages": len(reader.pages),
            "character_count": len(extracted_text.strip())
        }

    except Exception as error:

        raise ValueError(
            f"Unable to read PDF: {str(error)}"
        )