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
    if not os.path.exists(directory):
        return
    file_list = os.listdir(directory)
    for file in file_list:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            delete_files(file_path)


with open("head.md", "r", encoding="utf-8") as f:
    index_template = f.read()

with open("update.md", "r", encoding="utf-8") as f:
    update = f.read()

index_template += update

with open("end.md", "r", encoding="utf-8") as f:
    end_of_index = f.read()

source_path = r"./source"
display_path = r"./display"

with open("example.html", "r", encoding="utf-8") as f:
    slide_template = f.read()
