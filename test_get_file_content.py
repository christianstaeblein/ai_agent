from functions.get_file_content import get_file_content

def print_each(path:str):
    result = get_file_content("calculator", path)
    print(result)
    print(f"{path} length: {len(result)}")
    print(f"{path} truncated: {'truncated' in result}")


print_each("lorem.txt")
print_each("main.py")
print_each("pkg/calculator.py")
print_each("/bin/cat")
print_each("pkg/does_not_exist.py")
