---
- children:
    - |
        ## 乱讲珂朵莉树
        [原文地址 by @Wind_love](https://www.luogu.com.cn/article/1x3z9al4)。

        结合 [OI.wiki](OI.wiki) 和我的经验乱改的。

        应该没有瑕疵了，有的记得私信或喷我。

        > 乱改 by @[aaron0919](https://www.luogu.com.cn/user/818165)

        [这垃圾源码也有人要？$270+$ 行 $7000+$ Byte](https://www.luogu.me/paste/z6dqyaa5)
    - |
        ## 免责声明

        不好意思，例题全是某臭名昭著上的。但 UOJ 的幻灯片还是太高级了就放这了。

        >>> **本幻灯片无商业用途，仅供学习交流。**

        ~~其实是写来给xxs看的。~~

        写的不好可以喷，随便点差评，~~反正是写来给xxs看的。~~

        ！！竟然花了我 $5$ 个小时！！
- |
    ## 什么是 ODT

    珂朵莉树，颜色段均摊，由 [数据删除](https://www.luogu.com.cn/user/3296) 的 [CF896C](https://www.luogu.com.cn/problem/CF896C) 而得名。

    其核心思想是利用推平操作，将一个区间变为左端点，右端点，值三个量，用 `set` 或链表将其按左端点排序，从而将每段区间串联起来。

    这种数据结构极为暴力，它其实并不是一棵树，只是一个序列，但传统 ODT 在随机数据下可以达到均摊 $O(n\log n)$ 的优秀复杂度，`跳表/set`版本可以更快 $O(n\log\log n)$。以下介绍的 ODT，均为使用 `set` 实现的 ODT。

    [`map` 其实更短。](https://oi-wiki.org/misc/odt/#%E5%AE%9E%E7%8E%B0stdmap)
- |
    ## ODT 的原理

    将值相同的一段区间合并成一个结点处理。相较于传统的线段树等数据结构，对于含有区间覆盖的操作的问题，珂朵莉树可以更加方便地维护每个被覆盖区间的值。
- |
    ## ODT 的复杂度

    如果要保证复杂度正确，必须保证数据随机。详见 [Codeforces 上关于珂朵莉树的复杂度的证明](http://codeforces.com/blog/entry/56135?#comment-398940)。更详细的严格证明见 [珂朵莉树的复杂度分析](https://zhuanlan.zhihu.com/p/102786071)。证明的结论是：用 `std::set` 实现的珂朵莉树的复杂度为 $O(n \log \log n)$，而用链表实现的复杂度为 $O(n \log n)$。

- |
    ## ODT 的操作

    ODT 有两个基本操作，分裂和推平，即 `spilt` 和 `assign`。

    对于分裂操作，在 `set` 内二分目标点所在块，删除该块，插入从目标点分裂开的两个块，复杂度为 $O(\log n)$。

    对于推平操作，先将目标区间的两端分割下来，删除目标区间内所有块，插入一个由左端点，右端点，目标值组成的新块，复杂度与分裂相同。

    推平操作主要保证低复杂度，分裂操作用于获取区间。

    基于这两个操作，我们可以完成区间加，区间最值等许多操作。
- children:
    - |
        ## ODT 的简单实现

        (我的垃圾马蜂,不是大佬${\color{red}W}ind\_love$的)
    - |
        ### 节点

        种锁粥汁，`mutable` 是 `const` 的反义词。

        旧似嗦，我们可以直接修改已经插入 `set` 的元素的 `val` 值，而不用将该元素取出后重新加入 `set`。

        ```cpp
        struct nde
        {
            int l, r;
            mutable int val;
            bool operator<(const nde &other) const { return l < other.l; }
        };
        ```
    - |
        ### 初始化

        初始化时，向珂朵莉树中插入一个极长区间（如题目要求维护位置 $1$ 到 $n$ 的信息，插入区间 $[1,n+1]$）。
        ```cpp
        set<nde> s;
        int main()
        {
            cin >> n;
            s.insert({1, n + 1, 0});
        }
        ```
    - |
        ### 分裂
        将 $[l,r]$ 裂成 $[l,x),[x,r]$ 并返回后者。
        ```cpp
        auto split(int x)
        {
            auto p = s.lower_bound({x, 0, 0});
            if (p != s.end() && p->l == x)
            {
                return p;
            }
            --p;
            auto [l, r, val] = *p;
            s.erase(p);
            s.insert({l, x - 1, val});
            return s.insert({x, r, val}).first;
        }
        ```
    - |
        ### 推平
        有了 `split`，剩下的乱打就行了。

        因为有 `split(r + 1)` 这种东西，自然初始区间就要设为 $[1,n+1]$。

        ```cpp
        void assign(int l, int r, int x)
        {
            auto q = split(r + 1), p = split(l);
            s.erase(p, q);
            s.insert({l, r, x});
        }
        ```
    - |
        ### 例子-区间求和
        真的就是乱打，但注意先 `split` 右端点再 `split` 左端点。

        [肯定有人问为什么，因为会奇奇怪怪地 RE 掉。](https://oi-wiki.org/misc/odt/#assign-%E6%93%8D%E4%BD%9C:~:text=%E5%8C%BA%E9%97%B4%E5%88%A0%E5%8E%BB%EF%BC%8C-,%E4%BD%BF%E8%BF%AD%E4%BB%A3%E5%99%A8%E5%A4%B1%E6%95%88,-%E3%80%82)

        ```cpp
        int sum(int l, int r)
        {
            int res = 0;
            auto q = split(r + 1), p = split(l);
            for (auto it = p; it != q; ++it)
            {
                (res += it->val * (it->r - it->l + 1)) %= MOD;
            }
            return res;
        }
        ```
- |
    ## ODT可解决的问题

    一般来讲，珂朵莉树可解的问题要求必须有推平操作，且数据尽可能随机，否则可以被卡成平方。

    从 CF896C 这道老祖宗例题来讲，要求维护一个序列，支持区间加，区间推平，区间第 $k$ 小，区间次幂和。

    传统意义上讲，这类题目应该用线段树解决，但线段树不便维护区间次幂和，且码量较大，${\color{red}W}ind\_love$看到这题的唯一线段树做法暴力求了区间次幂和。

    但是如果使用珂朵莉树，只需要维护上述三个基本值，再配合上简单的暴力，就可以解决本题。

    [CF896C 的实现 by Wind_love](https://www.luogu.me/paste/tg3hb1to)。
- children:
    - |
        ## ODT的相关运用

        拎了一大堆我也不会的例题，凑合着讲讲吧。
    - |
        ## ODT与其他数据结构

        例题 [P8512](https://www.luogu.com.cn/problem/P8512)。

        和其他多数据结构结合的题目类似，这里主要是利用了 ODT 便于推平的特性。

        说白了，维护每个时间戳染的颜色对答案的贡献，如果覆盖了之前覆盖过的区间，则需要减去之前的贡献。

        就可以离线下来，通过前缀和求出答案。

        这样的题目有一个共性，就是每次操作的答案间必须有联系，而这种联系必须可以被其他数据结构或算法所维护，这类题目的关键就是找到并维护这种联系。

        [我的垃圾实现。](https://www.luogu.com.cn/record/223293051)
    - |
        ## ODT与树链剖分

        众所周知，一道数据结构题只要上树就变成了一道新题。

        例题 [P2146](https://www.luogu.com.cn/problem/P2146)。

        这题只需要维护区间推平与全局求和。

        注意到卸载和安装的方向，一个需要推平整个子树，另一个则是推平从当前点到根的路径。

        含有推平操作，则使用 ODT 更为简便，重链剖分后直接推平即可。

        [P2146 的实现 by Wind_love](https://www.luogu.com.cn/record/221669817)，[我的垃圾实现](https://www.luogu.com.cn/record/223295797)。

        更深一步，也更能体现 ODT 优势的树剖题是 [P2486](https://www.luogu.com.cn/problem/P2486)，读者自证[~~难明~~](https://www.luogu.com.cn/article/bs987nyq)不难。
    - |
        ## ODT 与区间翻转

        这例题是我找的，[我的垃圾提交记录](https://www.luogu.com.cn/record/list?pid=P5350&user=818165&page=1)，RE/MLE 了 $37$ 发。

        这题需要求和推平区间加，还有区间的翻转交换和复制。

        因为 ODT 使用 `set`，对区间进行了动态排序，所以很适合处理区间翻转的问题。

        在处理翻转操作时，只需要算出该区间左右边界在翻转后的位置，直接修改即可，记得交换左右边界。

        [P5350 的实现 by Wind_love](https://www.luogu.com.cn/record/188989778)。
    - |
        ## ODT 与区间复制和交换

        很自然的还是上题。

        然后再说一下如何实现区间复制和交换，复制比较简单，把原区间所有段拿出，删除目标区间内段，改变左右边界后将原区间内块插入即可。

        区间交换稍微复杂一点，需要将两个区间取出，在 ODT 中删除，再改变两区间内块的左右边界，最后插入即可。

        [我的乱打代码](https://www.luogu.com.cn/record/211324749)。

- children:
    - |
        ## ODT思想的推广

        ODT思想，即靠左右边界及一个或多个数值表示一个区间的思想。

        一般情况下，我们保存这个区间内数的值，但有时，这个数值还可以表示其他内容。

    - |
        ## 垃圾例题

        例题是 [P11833](https://www.luogu.com.cn/problem/P11833)，联合省选 D2T1，推箱子。

        按时间排序的贪心是容易想到的，这里讲后面的操作部分。

        我们注意到，把一排箱子一起推动后，其位置形成一个公差为 $1$ 的等差数列。

        则我们保存区间的首项，就可以表示出这个区间内的所有数。

        然后需要写比较复杂的模拟，求出每个箱子推完后的时间，判断是否满足限制即可。
  
        ~~很可惜，Wind_love 还有我在考场上都没有写出来。~~
        
        ~~所以太伤心了代码被我吃了。~~

    - |
        ## 高级进阶

        [自己看，太发散了。](https://www.luogu.com.cn/article/0mys9qkh)
- |
    ## 总结

    ODT 代码简单，思维暴力，适于维护易被表示的区间，但要求直接或间接有区间推平操作。

    同时，它可以简单的维护几乎所有线段树可维护的内容，在适当情况下可以代替其他数据结构使用。
- |
    ## 极其简单的例题

    1. [CF896C 开山鼻祖](https://www.luogu.com.cn/problem/CF896C)
    2. [P8512 ODT+fnw](https://www.luogu.com.cn/problem/P8512)
    3. [P2486 ODT+hld](https://www.luogu.com.cn/problem/P2486)
    4. [P2146 ODT+hld](https://www.luogu.com.cn/problem/P2146)
    5. [P5350 毒瘤操作 & RE 专场](https://www.luogu.com.cn/problem/P5350) 先做，能丧失对 ODT 的热情。
    6. [P11833 维护等差数列的 ODT](https://www.luogu.com.cn/problem/P11833)
    7. [P7983 ODT+分块](https://www.luogu.com.cn/problem/P7983)
    8. [P6749 维护等差数列的 ODT](https://www.luogu.com.cn/problem/P6749)
    9. [P5251 ODT+线段树](https://www.luogu.com.cn/problem/P5251)
    10. [P8146 ODT+分块+并查集+卡常](https://www.luogu.com.cn/problem/P8146)
    11. [P2823 区间排序+离线](https://www.luogu.com.cn/problem/P2824)

- children:
    - |
        ## 彩蛋

        记得去膜拜 @[Wind_love](https://www.luogu.com.cn/user/772368) 和 @[[数据删除]](https://www.luogu.com.cn/user/3296)。

        > 在太阳西斜的这个世界里，置身天上之森。等这场战争结束之后，不归之人与望眼欲穿的人们，人人本着正义之名。长存不灭的过去、逐渐消逝的未来，我回来了。纵使日薄西山，即便看不到未来，此时此刻的光辉，盼君勿忘。
        > > ----世上最幸福的女孩：珂朵莉
    - |
        ## ~~好题分享~~

        [我永远喜欢珂朵莉](https://www.luogu.com.cn/problem/P3987)

        ![](https://cdn.luogu.com.cn/upload/pic/11191.png)