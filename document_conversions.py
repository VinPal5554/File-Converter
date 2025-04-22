import os
import fitz  # PyMuPDF

# Convert PDF to TXT
def convert_pdf_to_txt(file_path):
    if not file_path.lower().endswith(".pdf"):
        raise ValueError("Please select a PDF file")
    output_file = os.path.splitext(file_path)[0] + ".txt"
    with fitz.open(file_path) as doc, open(output_file, "w", encoding="utf-8") as f:
        for page in doc:
            f.write(page.get_text())
    return output_file

