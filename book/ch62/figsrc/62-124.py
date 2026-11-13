import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def tower(x0, mid, mrole, d1, d2, head):
    text(ax, x0 + 13, 76, head, 'encre', 's')
    box(ax, x0, 18, 26, 11, 'fixe', label='ℚ')
    box(ax, x0, 40, 26, 11, mrole, label=mid)
    box(ax, x0, 62, 26, 11, 'resultat', label=r'$E$')
    arrow(ax, (x0 + 13, 29.5), (x0 + 13, 39.5), 'varie'); text(ax, x0 + 17, 34.5, d1, 'varie', 'm', ha='left')
    arrow(ax, (x0 + 13, 51.5), (x0 + 13, 61.5), 'varie'); text(ax, x0 + 17, 56.5, d2, 'varie', 'm', ha='left')
tower(4, r'ℚ($\sqrt[3]{2}$)', 'sujet', '×3', '×2', 'chemin 1')
tower(58, r'ℚ($j$)', 'autre', '×2', '×3', 'chemin 2')
text(ax, 44, 67.5, '=', 'resultat', 'xl')
box(ax, 14, 2, 60, 11, 'resultat', label=r'$3\times2=2\times3=6$')
save(fig, '62-124')
