---
- |
    # ABC 略结

    q(≧▽≦q)

    按时间降序排列...

- children:
    - |
        ## abc417

        <table><thead><tr><th class="sort-th no-break sort-asc" style="width: 3%;">Rank</th> <th class="sort-th no-break standings-th-user" style="min-width: 100px;">User</th>  <th class="sort-th no-break" style="width: 60px; min-width: 60px;">Score</th> <th class="sort-th no-break" style="width: 60px; min-width: 60px;"><a href="https://atcoder.jp/contests/abc417/tasks/abc417_a" target="_blank">A</a></th><th class="sort-th no-break" style="width: 60px; min-width: 60px;"><a href="https://atcoder.jp/contests/abc417/tasks/abc417_b" target="_blank">B</a></th><th class="sort-th no-break" style="width: 60px; min-width: 60px;"><a href="https://atcoder.jp/contests/abc417/tasks/abc417_c" target="_blank">C</a></th><th class="sort-th no-break" style="width: 60px; min-width: 60px;"><a href="https://atcoder.jp/contests/abc417/tasks/abc417_d" target="_blank">D</a></th><th class="sort-th no-break" style="width: 60px; min-width: 60px;"><a href="https://atcoder.jp/contests/abc417/tasks/abc417_e" target="_blank">E</a></th><th class="sort-th no-break" style="width: 60px; min-width: 60px;"><a href="https://atcoder.jp/contests/abc417/tasks/abc417_f" target="_blank">F</a></th><th class="sort-th no-break" style="width: 60px; min-width: 60px;"><a href="https://atcoder.jp/contests/abc417/tasks/abc417_g" target="_blank">G</a></th><th class="standings-result-th standings-perf" style="width:84px;min-width:84px;">Performance</th><th class="standings-result-th standings-rate" style="width:168px;min-width:168px;">Rating 变化</th></tr></thead><tr class="info"><td class="standings-rank"><span>630</span> <!----></td> <td class="standings-username"><!----> <img src="https://img.atcoder.jp/assets/flag/CN.png" class="img-flag-btn"> <!----> <a href="https://atcoder.jp/users/aaron_small" class="username"><!----> <img src="https://img.atcoder.jp/assets/user/user-blue-4.png" class="user-rating-stage-s"> <span class="user-blue">aaron_small</span></a> <span class="standings-user-btn"><a href=""><span aria-hidden="true" class="glyphicon glyphicon-eye-open black"></span></a> <a href="https://atcoder.jp/contests/abc417/submissions?f.User=aaron_small"><span aria-hidden="true" data-html="true" data-toggle="tooltip" title="view aaron_small's submissions" class="glyphicon glyphicon-search black"></span></a></span> <!----></td>  <td class="standings-result"><p><!----> <span class="standings-score">2000</span> <!----> <span class="standings-wa">(3)</span></p> <!----> <p>88:50</p></td> <td class="standings-result"><p><!----> <a href="https://atcoder.jp/contests/abc417/submissions/68124779"><span class="standings-ac">100</span></a> <!----> <!----></p> <!----> <p>18:44</p></td><td class="standings-result"><p><!----> <a href="https://atcoder.jp/contests/abc417/submissions/68125884"><span class="standings-ac">200</span></a> <!----> <!----></p> <!----> <p>20:21</p></td><td class="standings-result"><p><!----> <a href="https://atcoder.jp/contests/abc417/submissions/68127545"><span class="standings-ac">300</span></a> <!----> <!----></p> <!----> <p>22:58</p></td><td class="standings-result"><p><!----> <a href="https://atcoder.jp/contests/abc417/submissions/68152330"><span class="standings-ac">425</span></a> <!----> <!----></p> <!----> <p>73:50</p></td><td class="standings-result"><p><!----> <a href="https://atcoder.jp/contests/abc417/submissions/68134166"><span class="standings-ac">475</span></a> <!----> <!----></p> <!----> <p>35:15</p></td><td class="standings-result"><p><!----> <a href="https://atcoder.jp/contests/abc417/submissions/68146356"><span class="standings-ac">500</span></a> <!----> <span class="standings-wa">(3)</span></p> <!----> <p>59:54</p></td><td class="standings-result"><p><!----> <!----> <span>(0)</span> <!----></p> <!----> <!----></td><td class="standings-result standings-perf"><span class="user-blue">1750</span></td><td class="standings-result standings-rate"><span class="bold"><span class="user-blue">1909</span></span> → <span class="bold"><span class="user-blue">1890</span></span> <span class="grey">(-19)</span></td></tr></table>

        难受, 小号还行, 不放了...

    - |
        ## A-E
        
        简单题

        在 D 题卡了好长一会儿

    - | 
        ## F

        简单线段树版题, 区间求和, 区间推平.

        但是我没取模!!!

        于是给 `update` 和 `pushdown` 加了取模

        还是 WA 了...

        于是给 `query` 加了取模

        还是 WA 了...

        竟然 `pushup` 没取模

        大号吃了三发罚时, 掉了 $200$ 多名...

    - |
        ## G
        很类似于一道题, 
        
        GMOJ4211 【五校联考1day2】送你一颗圣诞树

        >再过三个多月就是圣诞节了，小R 想送小Y 一棵圣诞树作为节日礼物。因为他想让这棵圣诞树越大越好，所以当然是买不到能够让他满意的树的，因此他打算自己把这棵树拼出来。现在，小R 开始画这棵树的设计图纸了。因为这棵树实在太大，所以他采用了一种比较方便的方法。首先他定义了m+ 1 棵树T0 到Tm。最开始他只画好了T0 的图纸：就只有一个点，编号为0。接着，对于每一棵树Ti，他在第Tai 棵树的第ci 个点和第Tbi 棵树的第di 个点之间连上了一条长度为li 的边。在Ti 中，他保持Tai 中的所有节点编号不变，然后如果Tai 中有s 个节点，他会把Tbi 中的所有节点的编号加上s。终于，他画好了所有的树。现在他定义一颗大小为n 的树的美观度为,其中d(i; j) 为这棵树中i 到j 的最短距离。为了方便小R 选择等究竟拼哪一棵树，你可以分别告诉他T1 到Tm 的美观度吗？答案可能很大，请对10^9 + 7 取模后输出。

        很显然, 这道题并不是记搜, 因为交上去 TLE 了.

        正解: 树剖...