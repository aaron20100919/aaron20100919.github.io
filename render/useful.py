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


index_template = """---
- children:
    - |
        # Doctor. Aaron's 极简博客

        Welcome to my blog!!!

        > 本博客基于 `HTML5, CSS3, javascript, python` 等技术实现，欢迎访问！

        向右切幻灯片就是博客内容了，非常低级...
        
        全屏使用更佳

    - |
        ## 一些说明

        ~~其实就是纯手写，没有任何第三方库和样式，纯粹的原生`HTML5+CSS3+JS`~~

        ~~`python` 是用来线下手动渲染的...~~

        中英文标点符号混用.。.会显得很奇怪，但懒得改了.

        关于幻灯片渲染是因为觉得 UOJ 的幻灯片渲染太高级了，闲的蛋疼就自己弄了一个...

        [免费体验](app/slide.html)
- |
    主要内容：
    
    不定期更新有用没用有卵用没卵用自己捣鼓的垃圾项目。
    
    偶尔会写一些总结，总之会慢慢充实起来的。
"""


with open("example.html", "r", encoding="utf-8") as f:
    slide_template = f.read()
