---
- |
    # C++ 调试模板

    可以直接滚到最右边自取。

    结合了大量 C++11 和 C++14 的新特性，如有误欢迎 ~~*喷*~~ 指正。

- |
    ### 0. 最初的最初

    > 某一大群人用 vscode 不会调试，我告诉他下 `C/C++ Extension Pack` 和 `C/C++ Compile Run` 两个扩展，再把 `mingw64\bin` 添加到环境变量，F5 一键调试，他还告诉我挂了，我一看，竟然路径名中有中文。。。

    gdb 太高级了，不会。

- |
    ### 1. 所以直接输出

    如果运行时我想知道某个值的变化，怎么办？

    直接 `cout << x << '\n';` 或 `printf("%d\n", x);` 即可。

    但是调完后需要删掉或注释掉，不然直接 $100\to0$。

- |
    ### 2. 所以直接输出到错误流

    聪明的小孩子想到 `cerr/fprintf(stderr)`，嗯，这才是正确的做法。

    但是如果要输出很多个，前一种格式太烦了，后一种又太长了，怎么办。

    同时输出多了不知道哪一行对应的是哪一个，怎么办？？？

    慢慢来，一个一个解决。

- children:
    - |
        ### 3 所以用可变参数宏 & 可变参数函数模板

        #### 宏定义

        注意到宏定义支持字符串替换，举个例子。

        ```cpp
        #define debug(x) cerr << #x << " = " << (x) << '\n';
        ```

        如果我写 `debug(a + b)`，编译时就会自动替换为 `cerr << "a + b" << " = " << (a + b) << '\n';`。

        这样，我只需要在需要输出的地方写 `debug(x)` 即可。

        但是如果我要同时检查多个值，怎么办？

    - |

        #### [可变参数函数模板](https://oi-wiki.org/lang/new/#%E5%8F%AF%E5%8F%98%E5%8F%82%E6%95%B0%E5%87%BD%E6%95%B0%E6%A8%A1%E6%9D%BF)

        在 C++11 之前，类模板和函数模板都只能接受**固定**数目的模板参数。

        C++11 引入了模板参数包，可以接受**任意**数量和**任意**类型的模板参数。

        由于 `fprintf` 并不像 `cerr` 一样[**多态**](https://blog.csdn.net/weixin_44826356/article/details/105470565)，所以以下都用 `cerr` 实现。

        可变参数模板类似于：`template <typename... Clazz> void fun(Clazz... paras) {}`。

        所以我们可以这样输出多个值：

        ```cpp
        template <typename T>
        void debug(const T &t) { cerr << t << '\n'; }
        template <typename T, typename... Args>
        void debug(const T &t, const Args &...rest)
        {
            cerr << t << ' ';
            debug(rest...);
        }
        ```

        注意到需要一个**终止**函数，否则最后只剩一个参数时会报错。

        现在可以这样调用：`debug(a, b, a + b)`。

        突然发现输出成一行了更不知道谁是谁了，怎么办？？？

    - |

        #### 所以接着用宏定义

        **可变参数宏**，是一种类似于可变参数函数模版的宏定义。

        使用方法也很简单：`#define debug(...) _debug(#__VA_ARGS__ " =", __VA_ARGS__)` 就行了。

    - |

        #### 所以拼起来

        ```cpp
        template <typename T>
        void _debug(const T &t) { cerr << t << '\n'; }
        template <typename T, typename... Args>
        void _debug(const T &t, const Args &...rest)
        {
            cerr << t << ' ';
            _debug(rest...);
        }
        #define debug(...) _debug(#__VA_ARGS__ " =", __VA_ARGS__)
        ```

        这时候同样调用 `debug(a, b, a + b);` 就会展开成 `_debug("a, b, a + b" " =", a, b, a + b)`，完美解决以上问题。

        > 注：这里用了编译时自带的字符串拼接。

    - |

        #### 新问题

        其实并没有解决所有问题，因为即使输出到错误流，也是要时间的，详见[某道入门赛题](https://www.luogu.com.cn/problem/B3785)。

- |

    ### 4. 所以接着上宏定义

    如何不用时间？

    不执行就不用时间，所以如果在 oj 上评测，就可以使用 `ONLINE_JUDGE` 宏。

    例如我最常用的一个模板：

    ```cpp
    #ifdef ONLINE_JUDGE
        freopen("???.in", "r", stdin);
        freopen("???.out", "w", stdout);
    #endif
    ```

    本地测是不会重定向输入输出流的，教到 oj 上时会打开文操。

    直接套上：

    ```cpp
    #ifndef ONLINE_JUDGE
    template <typename T>
    void _debug(const T &t) { cerr << t << '\n'; }
    template <typename T, typename... Args>
    void _debug(const T &t, const Args &...rest)
    {
        cerr << t << ' ';
        _debug(rest...);
    }
    #define debug(...) _debug(#__VA_ARGS__ " =", __VA_ARGS__)
    #else
    #define debug(...) 0
    #endif
    ```

    这样在 oj 上放循环语句里的 `debug(x)` 都会替换为无用语句，不会影响程序运行效率（同时减少编译时间）。

- |

    #### 新问题

    所以输出数组还是要打 `for` 是吧。

    但是你可以用 `copy` 函数，原理我也不知道，反正可以这么用来输出一个数组：`copy(a + 1, a + 1 + n, ostream_iterator<int>(cerr, " ")), cerr << '\n';`。

    发现打起来很麻烦，又要注释，又不知道是哪个数组，怎么办？？？

- children:
    - |

        ### 5. 所以新建一个类（结构体）！！！

        好吧，我们先看看直接 `debug(a + 1, a + 1 + n);` 会输出什么？

        两坨指针，不用试了，那 `vector` 呢。

        直接 CE。

        > `no match for 'operator<<' (operand types are 'std::ostream' {aka 'std::basic_ostream<char>'} and 'const __gnu_cxx::__normal_iterator<long long int*, std::vector<long long int> >')`

        所以考虑新建一个类，再[重载输出流运算](https://www.runoob.com/cplusplus/input-output-operators-overloading.html)。

    - |

        结合之前的新特性，很轻松就能写出来：

        ```cpp
        template <typename Iterator>
        struct _Range
        {
            Iterator l, r;
            friend ostream &operator<<(ostream &os, const _Range &t)
            {
                if (t.l >= t.r)
                {
                    return os << "[]";
                }
                os << '[' << *t.l;
                for (auto i = next(t.l); i != t.r; ++i)
                {
                    os << ',' << *i;
                }
                return os << ']';
            }
        };
        ```

        兴高采烈的你试了试 `_Range(a.begin(), a.end())`，还是 CE。

        因为没有填充对应模板还是别的什么问题，反正怎么都调不出来。

        所以我们新建一个辅助函数，自动推导类型并填充进模板，同时支持 C-style 数组和 `vector` 等 STL 容器：

    - |

        为了自动推导类型，我们需要用到 [`auto` 和 `decltype` 关键字](https://oi-wiki.org/lang/new/)。

        这都是 C++14 的新特性，但我的主要目的并不是介绍新特性，自己看吧。

        ```cpp
        template <typename Container>
        auto Range(const Container &c, size_t l, size_t r) -> _Range<decltype(begin(c))>
        {
            auto start = begin(c) + min(l, c.size());
            auto end = begin(c) + min(r, c.size());
            return {start, end};
        }
        template <typename T, size_t N>
        auto Range(const T (&arr)[N], size_t l, size_t r) -> _Range<const T *> { return {arr + min(l, N), arr + min(r, N)}; }
        ```

        这样可以 `cerr << Range(a, 0, a.size())` 来输出整个 `vector` 了，是不是很又臭又长？

    - |

        所以我们再实现一个返回整个容器的辅助函数 `Range`：

        ```cpp
        template <typename Container>
        auto Range(const Container &c) -> _Range<decltype(begin(c))> { return {begin(c), end(c)}; }
        template <typename T, size_t N>
        auto Range(const T (&arr)[N]) -> _Range<const T *> { return {arr, arr + N}; }
        ```

        因为同时支持 C-style 数组，你可以这么用：

        ```cpp
        int a[] = {1, 1, 4, 5, 1, 4};
        debug(Range(a));
        ```

        明显的，`initializer_list` 和 `array` 也支持，不做过多演示。

- |

    #### 我还想输出 `pair`！！

    `pair` 没有 `begin/end` 函数，因此我平时都用 `array<int, 2>`。

    简单重载一下就行了。

    ```cpp
    template <typename T1, typename T2>
    ostream &operator<<(ostream &os, const pair<T1, T2> &p) { return os << '(' << p.first << ',' << p.second << ')'; }
    ```

    什么！！你想要输出 `tuple`？？？那你还不如自定义一个类（结构体）同时重载输出流运算符呢。

- |

    ### 6. debug 还是太长了！！！

    我直接【请输入文本】。

    ```cpp
    #define D debug
    #define Rg Range
    #define ifD(cond, ...)      \
        if (cond)               \
        {                       \
            debug(__VA_ARGS__); \
        }
    ```

- |

    ## 总结

    [聚合一！！召唤完全体！！](https://aaron20100919.github.io/code/debug.cpp)

    终于解决了，尽管赛时不会脑抽打一遍这种东西，但平时用起来还是挺方便的。

    赛时打到 3 就行了，因为建议**不要依赖** `ONLINE_JUDGE` 宏，删注释才是最保险的。

    所以点个赞再走吧！

    很难想象 C++ 更新了这么多支持多态的特性，但还是很开心能用到这些技巧。

    为了赛时能用，所以只用了 C++14 即以前的特性，如果有更优秀的实现方法，请不吝赐教。
