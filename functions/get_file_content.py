#imports
import os
from config import CHARACTER_LIMIT



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
