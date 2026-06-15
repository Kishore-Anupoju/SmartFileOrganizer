from organizer.content_reader import read_file
from organizer.ai_classifier import classify_content


files = [
    "test_files/resume.txt",
    "test_files/terraform.txt",
    "test_files/invoice.txt",
    "test_files/aws_notes.txt"
]


for file in files:

    content = read_file(file)

    category = classify_content(
        content
    )

    print(
        f"{file} -> {category}"
    )
