template = """---
- children:
    - |
        # Doctor. Aaron's 极简博客

        Welcome to my blog!!!

        > 本博客基于 `HTML5, CSS3, javascript, python` 等技术实现，欢迎访问！

        向右切幻灯片就是博客内容了，非常低级...

    - |
        ## 一些说明

        ~~其实就是纯手写，没有任何第三方库和样式，纯粹的原生`HTML5+CSS3+JS`~~

        ~~`python` 是用来线下手动渲染的...~~

        中英文标点符号混用.。.会显得很奇怪，但懒得改了.

        关于幻灯片渲染是因为觉得 UOJ 的幻灯片渲染太高级了，闲的蛋疼就自己弄了一个...

        [免费体验](app/slide.html)
"""

import os, renderSlide
from useful import *


if __name__ == "__main__":
    source_path = "slide\\source"
    source_files = os.listdir(source_path)

    display_path = "slide\\display"
    delete_files(display_path)

    other = """- |
    ## 杂项

"""

    cnt = 0

    for file in source_files:
        if file.endswith(".md"):
            name = file[:-3]
            path = os.path.join(source_path, file)
            print(path, os.path.join(display_path, name + ".html"))
            renderSlide.render_slide(
                path,
                os.path.join(display_path, name + ".html"),
            )
            cnt += 1
            other += f"    {cnt}. [{get_title(path)}](/display/{name}.html)\n"

    template += other

    template += """
- |
    # That's all!
    > Thanks for your visit!
"""

    with open("index.md", "w", encoding="utf-8") as f:
        f.write(template)

    renderSlide.render_slide("index.md", "index.html")
