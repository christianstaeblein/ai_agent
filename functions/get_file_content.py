#imports
import os
from config import CHARACTER_LIMIT

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads and returns the contents of a file relative to the working directory. Content is truncated if it exceeds the configured character limit.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        if not valid_target:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_dir, "r", encoding="utf-8") as f:
            content = f.read(CHARACTER_LIMIT)

            if f.read(1):
                content += (
                f'\n[...File "{file_path}" truncated '
                f'at {CHARACTER_LIMIT} characters]'
                )

        return content

    except Exception as e:
        return f"Error: {e}"
