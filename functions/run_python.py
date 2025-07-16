import os
import subprocess
from functions.get_files_info import in_working_directory, get_files_info, set_file_paths
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory, full_file_path = set_file_paths(working_directory, file_path)

    # Ensure that we are staying within our working directory
    if not in_working_directory(abs_working_directory, full_file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # Check if file exists
    if not os.path.isfile(full_file_path):
        return f'Error: File "{file_path}" not found.'
    
    # Checks if the file is a python file. 
    if not full_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    

    # Now... We break everything by allowing an AI agent rwx access to the directory
    try:
        arg = ["python3", full_file_path]
        if args:
            arg.extend(args)

        sub_return = subprocess.run(arg, capture_output=True, timeout=30, cwd=os.path.dirname(full_file_path))

        final_output = []

        if sub_return.stdout:
            final_output.append(f'STDOUT: {sub_return.stdout.decode("utf-8")}')

        if sub_return.stderr:
            final_output.append(f'STDERR: {sub_return.stderr.decode("utf-8")}')

        if sub_return.check_returncode():
            final_output.append(f"Process exited with code {sub_return.returncode}")

        return "\n".join(final_output)
    except Exception as e:
        return f"Error: executing Python file: {e}"