import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'sur $\mathbb{R}$ : pivot non nul $\rightarrow$ 1', 'encre', 's')
for y, a, b, n in [(40, 'diag(5, 3)', 'diag(1, 1)', 'rang 2'), (20, 'diag(5, 0)', 'diag(1, 0)', 'rang 1')]:
    box(ax, 2, y, 30, 12, 'sujet', label=a, size='s')
    arrow(ax, (33, y + 6), (43, y + 6), 'varie')
    box(ax, 44, y, 30, 12, 'resultat', label=b, size='s')
    text(ax, 81, y + 6, n, 'resultat', 's', weight='bold')
text(ax, 44, 7, 'seul invariant : le rang', 'resultat', 'm', weight='bold')
save(fig, '59-159')
