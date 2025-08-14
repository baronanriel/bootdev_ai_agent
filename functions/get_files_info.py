import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


def in_working_directory(working_directory, path):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(path)

    return full_path.startswith(abs_working_directory)

def set_file_paths(working_directory, directory):
    working_dir = os.path.abspath(working_directory)
    new_dir = os.path.join(working_dir, directory)

    return working_dir, new_dir


def get_files_info(working_directory, directory=''):
    working_dir, new_dir = set_file_paths(working_directory, directory)
    content_str = f"Result for '{directory}' directory: "

    # Validate the Inputs to ensure they are directories
    if not os.path.isdir(working_dir):
        content_str += f'\nError: "{working_directory}" is not a directory'
        return content_str
    
    if not os.path.isdir(new_dir):
        content_str += f'\nError: "{directory}" is not a directory'
        return content_str
    
    
    # Check if directory is in the working directory
    #if not os.path.abspath(new_dir).startswith(working_dir):
    if not in_working_directory(working_dir, new_dir):
        content_str += f'\nError: Cannot list "{directory}" as it is outside the permitted working directory'
        return content_str
    

    # Passed the validation tests, now process
    for contents in os.listdir(new_dir):
        content_path = os.path.join(new_dir, contents)
        content_size = os.path.getsize(content_path)
        content_isdir = str(os.path.isdir(content_path))
        content_str += f'\n{contents}: file_size={content_size} bytes, is_dir={content_isdir}'
    return content_str

