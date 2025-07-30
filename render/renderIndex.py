import os, renderSlide
from useful import *


def render(allpath, prepath, depth):
    global index_template
    things = os.listdir(allpath)
    # print(allpath, things)
    cnt = 0
    prepath = prepath.replace("\\", "/")
    htmls = f"""- |
    {"#" * depth} {prepath}
    
"""
    for thing in things:
        path = os.path.join(allpath, thing)
        if os.path.isdir(path):
            render(path, os.path.join(prepath, thing), depth + 1)
        else:
            if thing.endswith(".md"):
                name = thing[:-3]
                output_path = os.path.join(display_path, prepath, name + ".html")
                print(path.replace("\\", "/"), output_path.replace("\\", "/"))
                renderSlide.render_slide(path, output_path)
                cnt += 1
                htmls += (
                    f"    {cnt} [{get_title(path)}](/display/{prepath}/{name}.html)\n\n"
                )

    if cnt > 0:
        index_template += htmls


if __name__ == "__main__":
    delete_files(display_path)

    render(source_path, "", 1)

    index_template += end_of_index

    with open("index.md", "w", encoding="utf-8") as f:
        f.write(index_template)

    renderSlide.render_slide("./index.md", "./index.html")

    os.remove("./index.md")
