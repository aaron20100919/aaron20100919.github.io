---
- |
    # ARC 略结

    q(≧▽≦q)

    按时间降序排列...

- children:
    - |
        ## ARC 207

        诡异ICPC赛制混入.

    - |
        ### A

        $n\le100$, 因此 dp

        考虑转化.

        > Also, “the cost of all lamps with cost at least 1 decreases by 1” can be rephrased as “after ighting the i-th lamp, the final MP consumption decreases by the number of unlit lamps with cost t east i.”

        然后发现可以把 $a_i$ 先减到小于 $N$, 就可以跑 $N^4$ 的 dp。

    - |
        ### B

        构造, 但是题目歧义.

        但我没读错, 他们都把 `the sum of the numbers of all vertices` 看成点数了, 但实际是编号和.

        如果开日文就是 `頂点の番号の総和`.

        简单说就是 $n<6$ 无解, 否则构造二分图.

    - |
        ### C

        随机化可过.

        就是打一个 $O(n^2)$ 的 dp, 然后发现随机采样 $30$ 个点转移可过.

    - |
        ### D

        猎奇博弈论, 只保留里面 4x4/3x3/2x3 个点暴力...

    - |
        ### E

        不会.

- children:
    - |
        ## ARC 206

        神秘简单厂，竟然过了4题

    - |
        ### A

        简单题，3:25就切了

    - |
        ### B

        神秘排序。

        分开颜色做就行了。。

    - |
        ### C

        简单找性质题。

        神秘dp

    - |
        ### D

        小号吃了6罚

        就是构造，然后你猜k=0和k=1无解。。

        WA了

        然后你找出了k=1, `4 1 3 [5,n] 2`。

        然后交上去还是Wa。

        欸，k=0到底有没有解。

        100min的时候打了个暴力（暴力好难打）。

        ctnnd，n>=8才有解，然后就过了：`[n,9],3 4 8 7 2 1 5 6`

    - |
        ### E

        太难了


- children:
    - |
        ## ARC 203

        不小心错过了，没 rated。

    - |
        ### A+B
        
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

    - |
        ### D

        死磕 C 然后没想到有长为 $H+W$ 的路径于是挂了。

        考虑倒着删数。

        首先特判掉全为 $1$ 的情况，然后就有以下情况：

        1. $1,1$ 很显然前后至少有一个 $0$ 就可以删掉一个 $1$；
        2. $0,0,\dots,0$ 若干个 $0$ 中间的显然可以删；
        3. $1,0,1$ 前后至少有一个 $0$ 就可以删掉一个 $0$ 和一个 $1$。

    - |
        我们这样定义 $A_i$ 的贡献（与上面一一对应）：

        $$
        \begin{cases}
        -1 & \text{if } A_{i-1}=1\land A_i=1 \\
        -1 & \text{if } A_{i-1}=0\land A_i=0 \land A_{i+1}=0 \\
        -2 & \text{if } A_{i-1}=1\land A_i=0 \land A_{i+1}=1 \\
        \end{cases}
        $$

        为什么 $1,0,1$ 的贡献是 $-2$，因为后面那个 $1$ 并不会经过情况一造成贡献，于是就加进 $0$ 的贡献。

        注意到 $1,0,1$ 的情况并没有考虑到只有一个 $0$，所以如果答案减成了 $1$ 就要输出 $2$。
    
    - |

        ### E

        模 $L$ 染色，然后被我咕掉了。
