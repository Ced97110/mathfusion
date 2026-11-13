import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# trois ensembles de tableaux à cases entières : 2 × 3, 3 × 2, 2 × 2
s = 7.0
def grid(x, y, n, m, role):
    for j in range(n):
        for i in range(m):
            box(ax, x + i * s, y + (n - 1 - j) * s, s - 0.9, s - 0.9, role, r=0.3, lw=0.7)
text(ax, 44, 59, r'$M_{n,m}(R)$ : $n$ lignes, $m$ colonnes', 'encre', 'm', weight='bold')
specs = [(6, 2, 3, 'sujet'), (36, 3, 2, 'autre'), (62, 2, 2, 'varie')]
for x, n, m, role in specs:
    grid(x, 24, n, m, role)
    cx = x + m * s / 2 - 0.45
    text(ax, cx, 17, r'$M_{%d,%d}(\mathbb{Z})$' % (n, m), role, 's', weight='bold')
    text(ax, cx, 11, r'$n = %d$, $m = %d$' % (n, m), role, 's')
save(fig, '58-209')
