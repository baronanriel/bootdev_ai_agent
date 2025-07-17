import os
from google.genai import types
from functions.get_files_info import get_files_info, in_working_directory, set_file_paths

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites the provided content to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="This is the file path of the file to be written to."
            ),
            "content": types.Schema(
                type = types.Type.STRING,
                description="The content to write to the file"
            )
        },
        required = ["file_path", "content"]
    ),
)

def write_file(working_directory, file_path, content):
    abs_working_directory, full_file_path = set_file_paths(working_directory, file_path)

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
    
