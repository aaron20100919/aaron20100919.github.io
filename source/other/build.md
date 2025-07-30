---
- |
    # 如何搭建一个像这样的博客

    你要有的东西有: github账户, python 3.2+ 的环境, 还要下个 git.

    运行 `python` 和 `bat` 文件请在 `***.github.io` 路径下运行
- |
    ## 准备

    首先, 你先 clone 整个仓库到本地, 在 github 上建一个名为 `{YOURGITHUBUSERNAME}.github.io` 的仓库.

    然后删了整个 `.git` 目录

    然后自行搜索教程将 git 绑定到你自己的仓库.

- |
    ## 如何改成自己的博客

    请确保主目录下的 `*.md` 都在, 以及 `example.html` 也不能删, 一定要保留 `render` 和 `source` 目录.

    你需要修改的部分有:

    1. 搜索 `https://cdn.luogu.com.cn/upload/image_hosting/30orb1d0.png` 并换成你的头像
    2. 如果你 ~~厚颜无耻~~ 懒的话, 直接将所有 `aaron20100919` 替换为你的用户名
    3. ~~如果你干了步骤 2, 给我保留个 `example.html` 文件中的 `<footer>` 部分吧~~
    4. 清空 `source` 下的内容, 如果你要写, 请务必再建一层目录
    5. 想要修改页面样式请修改 `example.html` 中的内容
    6. 想要修改更新日志请修改 `update.md` 中的内容
    7. 想要修改 `index.html` 的内容请修改 `head.md` 和 `end.md` 中的内容

- |
    ## 注意事项

    > 加个原作者名字吧

    所有 `markdown` 文件除了 `README.md` 都要用幻灯片的语法来写, 修改完后都要 `build` 一下.

    ~~其实可以用 markdown 的语法写, 会渲染成一页的幻灯片~~

    [如何写呢?](/display/other/slide.html)

    写完后可先本地 `build.bat`, 然后本地看看, 没问题就 `push.bat`

    引用图片可以放在 `image` 里, 写了 `html` 网页就放 `app` 里, 剩下的最好不要动

    >> $\text{\color{red}一定要先 build, 在 push!!}$

- |
    ### 一些奇奇怪怪但是需要注意的事

    `display` 目录和 `index.html` 都是通过 `build` 自动更新的, 不要改错了...
