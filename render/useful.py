import os, re


def get_title(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        res = re.search(r"# (.+)\n", content)
        if res:
            return res.group(1)
        else:
            return re.sub(r"\.md$", "", os.path.basename(filename))


def delete_files(directory):
    file_list = os.listdir(directory)
    for file in file_list:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
