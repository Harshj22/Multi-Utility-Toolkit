import os

def create_file():
    file_name = input("Enter file name: ")
    if file_name.strip() == "":
        print("File name cannot be empty.")
        return

    if os.path.exists(file_name):
        print("File already exists.")
    else:
        with open(file_name, "w", encoding="utf-8"):
            pass
        print("File created successfully.")


def write_file():
    file_name = input("Enter file name: ")
    data = input("Enter data to write: ")
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(data)
        print("Data written successfully.")
    except FileNotFoundError:
        print("File not found. Please create the file first.")


def read_file():
    file_name = input("Enter file name: ")
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print("File not found.")


def append_file():
    file_name = input("Enter file name: ")
    data = input("Enter data to append: ")
    try:
        with open(file_name, "a", encoding="utf-8") as f:
            f.write("\n" + data)
        print("Data appended successfully.")
    except FileNotFoundError:
        print("File not found.")

