#imports
import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Creates or overwrites a file within the working directory and writes the provided content to it. Missing parent directories are created automatically.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The text content to write to the file",
                },
            },
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        if not valid_target:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        #create missing parent folders
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)

        #write the content
        with open(target_dir, "w", encoding="utf-8") as f:
            f.write(content)
            return f'Successfully wrote to "{target_dir}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
