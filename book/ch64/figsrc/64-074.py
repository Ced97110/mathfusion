import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'dans $\mathbb{Z}$ : on descend sans fin', 'varie', 'm')
f = numberline(ax, 20, 76, 14, 0, 16, step=2, every=2, arrow_right=False)
for y, m in [(54, 2), (44, 4), (34, 8), (24, 16)]:
    text(ax, 9, y, rf'${m}\mathbb{{Z}}$', 'sujet', 'm')
    for v in range(0, 17, m):
        disc(ax, f(v), y, 1.2, 'sujet')
    line(ax, [(18, y), (f(16) + 1, y)], 'fixe', lw=0.4)
text(ax, 44, 4, r'$\{0\}$ jamais atteint', 'limite', 'm', weight='bold')
save(fig, '64-074')
