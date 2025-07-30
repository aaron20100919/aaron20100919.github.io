import os
from useful import *


def render_slide(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
        title = get_title(input_file)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(
                slide_template.replace("{{title}}", title).replace(
                    "{{content}}", content
                )
            )


if __name__ == "__main__":
    input_file = input("Input file path: ")
    output_file = input_file[:-3] + ".html"
    render_slide(input_file, output_file)
    print(f"Slide rendered to {output_file}")
