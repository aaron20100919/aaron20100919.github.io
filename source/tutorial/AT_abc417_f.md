---
- |
    # AT_abc417_f の题解

    简单线段树板题。

- |

    ## 题意

    有 $N$ 个盘子初始各有石子，进行 $M$ 次操作，每次操作移除区间 $[L_i, R_i]$ 内所有石子的总和，并随机选一个该区间内的盘子放回这些石子，求最终每个盘子的期望石子数，结果模 $998244353$。

- |

    ## 分析

    实际上随机选一个就等价于平均分了，所以考虑用线段树实现。

- |

    ## 实现

    需要实现区间推平，区间求和，打起来还是很简单的。

    注意取模，我就因为这个吃了 $3$ 发罚时。

- |

    ## 补充

    为了提高效率，我通常都会 `define` 一堆东西，有需要的自取，打起来就很爽。

    ```cpp
    #define mid (l + r) / 2
    #define ls (u << 1)
    #define rs (ls | 1)
    #define tu t[u]
    #define lu t[ls]
    #define ru t[rs]
    #define fl ls, l, mid
    #define fr rs, mid + 1, r
    ```

- |

    ## code

    可以滚动。

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    using ll = long long;
    #define int ll

    const int N = 1e6 + 10;
    const int INF = 1e18;
    const int MOD = 998244353;

    int n, m;
    int a[N], t[N][2];

    #define mid (l + r) / 2
    #define ls (u << 1)
    #define rs (ls | 1)
    #define tu t[u]
    #define lu t[ls]
    #define ru t[rs]
    #define fl ls, l, mid
    #define fr rs, mid + 1, r

    ll qpow(ll a, ll b = MOD - 2)
    {
        ll res = 1;
        while (b)
        {
            if (b & 1)
            {
                res = res * a % MOD;
            }
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    void pushup(int u)
    {
        tu[0] = (lu[0] + ru[0]) % MOD;
    }

    void pushdown(int u, int l, int r)
    {
        if (tu[1])
        {
            lu[0] = (mid - l + 1) * tu[1] % MOD;
            ru[0] = (r - mid) * tu[1] % MOD;
            lu[1] = ru[1] = tu[1];
            tu[1] = 0;
        }
    }

    void build(int u, int l, int r)
    {
        if (l == r)
        {
            tu[0] = a[l];
            return;
        }
        build(fl), build(fr);
        pushup(u);
    }

    void update(int u, int l, int r, int ql, int qr, int z)
    {
        if (ql <= l && r <= qr)
        {
            tu[0] = (r - l + 1) * z % MOD;
            tu[1] = z;
            return;
        }
        if (qr < l || r < ql)
        {
            return;
        }
        pushdown(u, l, r);
        update(fl, ql, qr, z), update(fr, ql, qr, z);
        pushup(u);
    }

    int query(int u, int l, int r, int ql, int qr)
    {
        if (ql <= l && r <= qr)
        {
            return tu[0];
        }
        if (qr < l || r < ql)
        {
            return 0;
        }
        pushdown(u, l, r);
        return (query(fl, ql, qr) + query(fr, ql, qr)) % MOD;
    }

    void print(int u, int l, int r)
    {
        if (l == r)
        {
            cout << tu[0] << ' ';
            return;
        }
        pushdown(u, l, r);
        print(fl), print(fr);
    }

    signed main()
    {
        cin.tie(0)->sync_with_stdio(false), cout.setf(ios::fixed), cout.precision(10);

        cin >> n >> m;
        for (int i = 1; i <= n; i++)
        {
            cin >> a[i];
        }
        build(1, 1, n);
        for (int i = 1, l, r; i <= m; i++)
        {
            cin >> l >> r;
            int sum = query(1, 1, n, l, r);
            update(1, 1, n, l, r, sum * qpow(r - l + 1) % MOD);
        }
        print(1, 1, n);

        return 0;
    }
    ```