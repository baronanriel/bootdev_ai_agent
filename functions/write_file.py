import os
from functions.get_files_info import get_files_info, in_working_directory

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.join(abs_working_directory, file_path)

    if not in_working_directory(abs_working_directory, full_file_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(os.path.dirname(full_file_path)):
            os.makedirs(os.path.dirname(full_file_path))
    except:
        return f'Error: Unable to create the new directory for "{file_path}"'
    
    try:
        with open(full_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return f'Error: Unable to write to "{file_path}"'