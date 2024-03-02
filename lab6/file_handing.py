import os
import string

'''
#Write a Python program to list only directories, files and all directories, files in a specified path.
def list_directories_and_files(path):
    directories = []
    files = []

    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            directories.append(item)
        else:
            files.append(item)

    print("Directories:")
    for directory in directories:
        print(directory)

    print("\nFiles:")
    for file in files:
        print(file)

    print("\nAll directories and files:")
    for item in os.listdir(path):
        print(item)


path = "/path/to/your/directory"

list_directories_and_files(path)

#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def check_path_access(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    print("Path exists.")

    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not readable")

    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not writable")

    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not executable")

path = "/path/to/your/directory"

check_path_access(path)

def test_path(path):
    if os.path.exists(path):
        print("Path exists.")
        directory, filename = os.path.split(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Path does not exist.")

path = "/path/to/your/file_or_directory"

test_path(path)

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return -1
    except IOError:
        print("Error reading the file.")
        return -1

file_path = "example.txt"

num_lines = count_lines(file_path)
if num_lines != -1:
    print(f"Number of lines in the file: {num_lines}")

def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print("List written to file successfully.")
    except IOError:
        print("Error writing to file.")

my_list = ['apple', 'banana', 'orange', 'grape']

file_path = "output.txt"

write_list_to_file(file_path, my_list)

def generate_files():
    for letter in string.ascii_uppercase:
        file_name = letter + ".txt"
        with open(file_name, 'w') as file:
            file.write("This is file " + letter)

generate_files()
'''
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")
    except IOError:
        print("Error copying the file.")


source_file_path = "source.txt"
destination_file_path = "destination.txt"

copy_file(source_file_path, destination_file_path)

def delete_file(path):
    if not os.path.exists(path):
        print("File does not exist.")
        return
    elif not os.access(path, os.F_OK):
        print("No access to the file.")
        return

    try:
        os.remove(path)
        print("File deleted successfully.")
    except OSError as e:
        print(f"Error deleting the file: {e}")
deleted
file_path = "/path/to/your/file.txt"

delete_file(file_path)