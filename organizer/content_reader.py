from pathlib import Path

from pypdf import PdfReader
from docx import Document


def read_file(file_path):

    file_path = Path(file_path)

    extension = file_path.suffix.lower()

    try:

        if extension == ".txt":
            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:
                return file.read()

        elif extension == ".pdf":

            reader = PdfReader(file_path)

            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

            return text

        elif extension == ".docx":

            document = Document(file_path)

            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

            return text

        else:
            return ""

    except Exception as error:

        print(
            f"Error reading {file_path}: {error}"
        )

        return ""