import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        if not valid_target:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'


        lines = []

        def walk(target_dir, indent=""):
            for item in os.scandir(target_dir):
                lines.append(
                    f"{indent}- {item.name}: "
                    f"file_size={item.stat().st_size} bytes, "
                    f"is_dir={item.is_dir()}"
                )

                if item.is_dir():
                    walk(item.path, indent + "")

        walk(target_dir)

        return "\n".join(lines)



    except Exception as e:
        return f"Error: {e}"
