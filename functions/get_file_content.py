import os
from functions.config import MAX_CHARS
from functions.get_files_info import get_files_info, in_working_directory, set_file_paths

def get_file_content(working_directory, file_path):
    abs_working_directory, full_file_path = set_file_paths(working_directory, file_path)
    
    # Ensuring the file is in our allowed working directory
    if not in_working_directory(abs_working_directory, full_file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Ensuring the file is, in fact, a file
    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # Read the contents of the file
    try:
        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

    
    except:
        return f'Error: Failed to read "{file_path}"'
    
    return file_content_string