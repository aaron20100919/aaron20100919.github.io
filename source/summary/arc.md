---
- |
    # ARC 略结

    q(≧▽≦q)

    按时间降序排列...

- children:
    - |
        ## ARC 203

        不小心错过了，没 rated。

    - |
        ### A

        简单，没什么好解析的。

    - |
        ### B

        简单，没什么好解析的。

    - |
        ### C

        赛时死活想不到为什么会有路径长为 $H+W$ 的，根本想不到，以下用 $n,m$ 代替 $H,W$。

        官方题解讲的似乎不是很清楚，我主要补充。

        最简单的部分就不赘述了。

        $$
        ans = \begin{cases}
            0 & \text{if } k < n + m - 2 \\
            \binom{n + m - 2}{n - 1} & \text{if } k = n + m - 2 \\
            \binom{n + m - 2}{n - 1} \cdot \binom{n(m - 1) + m(n - 1) - (n + m - 2)}{1} & \text{if } k = n + m - 1 \\
            ??? & \text{if } k = n + m
        \end{cases}
        $$

    - |

        考虑 $???$ 应该是什么。

        先统计路径长为 $n+m-2$ 的方案数，也就是 $k=m+n-1$ 是再多选一条边，也就是 $\binom{n + m - 2}{n - 1} \cdot \binom{n(m - 1) + m(n - 1) - (n + m - 2)}{2}$。

        但是可能会有重复的，考虑是什么情况。

        ~~根本画不出图，被我咕掉了。~~

        就是会把 $2\times2$ 的小矩阵打穿，这样就有两条路，但是两条路都会算一遍，要减掉。

        所以应该减去所有打穿小矩阵的方案数 $\binom{n+m-4}{n-2}\cdot(n+m-3)$。

        啊，不管了，下面的才是重点。

        ***

        还差路径长度为 $n+m$ 的情况，就是多一个 $\leftrightarrows$ 或 $\uparrow\downarrow$ 的情况。

        这又应该怎么算，考虑看成一个最短路再多折回一次。


    - |
        举个多一个 $\uparrow\downarrow$ 的情况的例子：

        | $\downarrow$  |               |               |               |              |
        | :-----------: | :-----------: | :-----------: | :-----------: | :----------: |
        | $\rightarrow$ | $\rightarrow$ | $\rightarrow$ | $\rightarrow$ | $\downarrow$ |
        |               |               |               |               |   $(n,m)$    |

        多加两行。

        | $\downarrow$  |               |                    |                    |              |
        | :-----------: | :-----------: | :----------------: | :----------------: | :----------: |
        | $\rightarrow$ | $\downarrow$  |                    |                    |              |
        |               | $\rightarrow$ | $\blue\rightarrow$ | $\blue\downarrow$  |              |
        |               |               |                    | $\blue\rightarrow$ | $\downarrow$ |
        |               |               |                    |                    |  $(n+2,m)$   |

        把其中一个 $\downarrow$ 翻成 $\uparrow$ 就得到了 $\uparrow\downarrow$ 的情况。

    - |
        
        | $\downarrow$  |               |                   |                   |              |
        | :-----------: | :-----------: | :---------------: | :---------------: | :----------: |
        | $\rightarrow$ | $\downarrow$  |                   | $\red\rightarrow$ | $\downarrow$ |
        |               | $\rightarrow$ | $\red\rightarrow$ |  $\red\uparrow$   |   $(n,m)$    |

        注意翻转时（蓝到红）$\downarrow$ 的前后必须都是 $\rightarrow$，把它们捆到一起来计算。
        
        这个部分等价于官方题解讲得不明不白的地方，同时也解释了第一个和最后一个 $\downarrow$ 为什么不能翻转：

        > Consider the case where this direction is vertical. When the shortest path length is $H+W$, the movements before and after this move must be horizontal. If we replace these H-V-H movements with V’, we can see that this corresponds to arranging $H+1$ V and $W-3$ H movements, then replacing one of the $2$\-nd to $H$\-th V movements with V’.  

        多一个 $\leftrightarrows$ 的答案是类似的，拼起来就是 $(n-1) \cdot \binom{n+m-2}{m-3} + (m-1) \cdot \binom{n+m-2}{n-3}$。
        
    - |
        把他们都拼起来，就能召唤 AC 了！

        $$
        ans = \begin{cases}
            0 & \text{if } k < n + m - 2 \\
            \binom{n + m - 2}{n - 1} & \text{if } k = n + m - 2 \\
            \binom{n + m - 2}{n - 1} \cdot \binom{n(m - 1) + m(n - 1) - (n + m - 2)}{1} & \text{if } k = n + m - 1 \\
            \binom{n + m - 2}{n - 1} \cdot \binom{n(m - 1) + m(n - 1) - (n + m - 2)}{2}-\binom{n+m-4}{n-2}\cdot(n+m-3)+ (n-1) \cdot \binom{n+m-2}{m-3} + (m-1) \cdot \binom{n+m-2}{n-3}& \text{if } k = n + m \\
        \end{cases}
        $$

        [代码自取。](https://atcoder.jp/contests/arc203/submissions/68218962)

