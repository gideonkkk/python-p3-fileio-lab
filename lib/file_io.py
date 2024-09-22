def write_file(file_name, file_content):
    file_name = str(file_name)
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, mode='w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, file_content):
    file_name = str(file_name)
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, mode='a', encoding='utf-8') as file:
        file.write(file_content)

def read_file(file_name):
    file_name = str(file_name)
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, mode='r', encoding='utf-8') as file:
        return file.read()

    return content
