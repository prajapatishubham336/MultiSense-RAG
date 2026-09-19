from pathlib import Path
import io
import fitz
import pytesseract
from PIL import Image
from docx import Document

def extract_content(uploaded_file):
    name = uploaded_file.name
    suffix = Path(name).suffix.lower()
    data = uploaded_file.getvalue()

    if suffix == ".pdf":
        pdf = fitz.open(stream=data, filetype="pdf")
        text = "\n".join(page.get_text() for page in pdf)
        if not text.strip():
            for page in pdf:
                pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
                image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                text += "\n" + pytesseract.image_to_string(image)
        return text, name

    if suffix in {".png", ".jpg", ".jpeg"}:
        return pytesseract.image_to_string(Image.open(io.BytesIO(data))), name

    if suffix == ".docx":
        doc = Document(io.BytesIO(data))
        return "\n".join(p.text for p in doc.paragraphs), name

    return data.decode("utf-8", errors="ignore"), name
