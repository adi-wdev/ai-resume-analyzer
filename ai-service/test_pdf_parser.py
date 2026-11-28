from pdf_parser import extract_text_from_pdf

with open("sample_resume.pdf", "rb") as file:

    pdf_bytes = file.read()

result = extract_text_from_pdf(pdf_bytes)

print("Message:", result["message"])

print("\nTotal Pages:", result["total_pages"])

print("\nCharacter Count:", result["character_count"])

print("\nExtracted Resume Text:")

print(result["extracted_text"])