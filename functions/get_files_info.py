import os


def get_files_info(working_directory, directory=None):
    working_dir = os.path.abspath(working_directory)
    new_dir = os.path.join(working_dir, directory)

    content_str = f"Result for '{directory}' directory: "

    # Validate the Inputs to ensure they are directories
    if not os.path.isdir(working_dir):
        content_str += f'\nError: "{working_directory}" is not a directory'
        return content_str
    
    if not os.path.isdir(new_dir):
        content_str += f'\nError: "{directory}" is not a directory'
        return content_str
    
    
    # Check if directory is in the working directory
    if not os.path.abspath(new_dir).startswith(working_dir):
        content_str += f'\nError: Cannot list "{directory}" as it is outside the permitted working directory'
        return content_str
    

    # Passed the validation tests, now process
    for contents in os.listdir(new_dir):
        content_path = os.path.join(new_dir, contents)
        content_size = os.path.getsize(content_path)
        content_isdir = str(os.path.isdir(content_path))
        content_str += f'\n{contents}: file_size={content_size} bytes, is_dir={content_isdir}'
    return content_str
