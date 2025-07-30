import os, renderSlide
from useful import *


if __name__ == "__main__":
    source_path = "source"
    source_folders = os.listdir(source_path)

    print(source_folders)

    display_path = "display"
    delete_files(display_path)

    for folder in source_folders:
        htmls = f"""- |
    ## {folder}

"""

        folder_path = os.path.join(source_path, folder)
        source_files = os.listdir(folder_path)

        cnt = 0

        for file in source_files:
            if file.endswith(".md"):
                name = file[:-3]
                path = os.path.join(folder_path, file)
                print(path, os.path.join(display_path, folder, name + ".html"))
                renderSlide.render_slide(
                    path,
                    os.path.join(display_path, folder, name + ".html"),
                )
                cnt += 1
                htmls += f"    {cnt} . [{get_title(path)}](/display/{folder}/{name}.html)\n\n"

        index_template += htmls

    index_template += """
- |
    # That's all!
    > Thanks for your visit!
"""

    with open("index.md", "w", encoding="utf-8") as f:
        f.write(index_template)

    renderSlide.render_slide("./index.md", "./index.html")

    os.remove("./index.md")
