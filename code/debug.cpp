#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll

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
template <typename Container>
auto Range(const Container &c) -> _Range<decltype(begin(c))> { return {begin(c), end(c)}; }
template <typename T, size_t N>
auto Range(const T (&arr)[N]) -> _Range<const T *> { return {arr, arr + N}; }
template <typename Container>
auto Range(const Container &c, size_t l, size_t r) -> _Range<decltype(begin(c))>
{
    auto start = begin(c) + min(l, c.size());
    auto end = begin(c) + min(r, c.size());
    return {start, end};
}
template <typename T, size_t N>
auto Range(const T (&arr)[N], size_t l, size_t r) -> _Range<const T *> { return {arr + min(l, N), arr + min(r, N)}; }
template <typename T1, typename T2>
ostream &operator<<(ostream &os, const pair<T1, T2> &p) { return os << '(' << p.first << ',' << p.second << ')'; }
#define D debug
#define Rg Range
#define ifD(cond, ...)      \
    if (cond)               \
    {                       \
        debug(__VA_ARGS__); \
    }

signed main()
{
    int a[] = {1, 1, 4, 5, 1, 4, 1, 9, 1, 9, 8, 1, 0};
    vector<int> b(a + 3, a + 10);
    array<int, 7> c = {1, 9, 1, 9, 8, 1, 0};

    static_assert(__cplusplus >= 201402L, "C++14 or higher required");

    // Some test cases
    debug(Range(a));                                   // Entire C-array
    debug(Range(a, 3, 10));                            // Subrange of C-array
    debug(Range(b));                                   // Entire vector
    debug(Range(b, 1, 4));                             // Subrange of vector
    debug(Range(a, 0, 3), Range(b), Range(a, 10, 13)); // Multiple ranges
    debug(make_pair(114514, "1919810"));               // Pair
    debug(Range({78, 1, 1, 4, 5, 1, 4, 91}, 1, 7));    // Range from initializer list
    debug(Range(c));                                   // Range from array

    // Group test cases
    int x = 1;
    string y = "145";
    ifD(114514 != 1919810, x, y, Rg(y, 0, 2), make_pair('1', "9"), Rg({"19", "81", "0"})); // Mix it all up
    ifD(114514 == 1919810, "What the hell?", 114514, '=', 1919810);                        // The condition is false

    return 0;
}
/*
Expected output:
Range(a) = [1,1,4,5,1,4,1,9,1,9,8,1,0]
Range(a, 3, 10) = [5,1,4,1,9,1,9]
Range(b) = [5,1,4,1,9,1,9]
Range(b, 1, 4) = [1,4,1]
Range(a, 0, 3), Range(b), Range(a, 10, 13) = [1,1,4] [5,1,4,1,9,1,9] [8,1,0]
make_pair(114514, "1919810") = (114514,1919810)
Range({78, 1, 1, 4, 5, 1, 4, 91}, 1, 7) = [1,1,4,5,1,4]
Range(c) = [1,9,1,9,8,1,0]
x, y, Range(y, 0, 2), make_pair('1', "9"), Range({"19", "81", "0"}) = 1 145 [1,4] (1,9) [19,81,0]
*/