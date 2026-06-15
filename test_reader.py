from organizer.content_reader import read_file

files = [
    "test_files/resume.txt",
    "test_files/terraform.txt",
    "test_files/invoice.txt"
]

for file in files:

    print("\n" + "=" * 40)

    print(file)

    print("-" * 40)

    content = read_file(file)

    print(content)
