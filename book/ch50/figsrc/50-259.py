import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def row(y, p, cells, head, res, rr):
    text(ax, 44, y + 17, head, 'fixe', 's')
    text(ax, 8, y + 4.5, p, 'sujet', 'l', weight='bold')
    for i, (v, r) in enumerate(cells): box(ax, 18 + 12 * i, y, 9, 9, r, label=v, size='m')
    arrow(ax, (18 + 12 * len(cells) + 1, y + 4.5), (48, y + 4.5), 'fixe')
    text(ax, 50, y + 4.5, res, rr, 'l', ha='left', weight='bold')
row(40, r'$n_7$', [('1', 'resultat'), ('3', 'limite')], 'divise 3 et reste 1 par 7', r'$n_7 = 1$', 'resultat')
row(12, r'$n_3$', [('1', 'resultat'), ('7', 'resultat')], 'divise 7 et reste 1 par 3', r'$n_3 \in \{1, 7\}$', 'varie')
save(fig, '50-259')
