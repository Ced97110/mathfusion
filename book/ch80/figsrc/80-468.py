import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
cols = [18, 46, 74]
for c, h, r in zip(cols, ['somme', 'calcul', 'valeur'], ['sujet', 'varie', 'resultat']):
    text(ax, c, 64, h, r, 'm', weight='bold')
rows = [('1', '1', '1'), ('3', r'$3-1$', '2'), ('6', r'$6-1-2$', '3')]
for i, (s, c, v) in enumerate(rows):
    y = 8 + i * 16 + 4
    y = 14 + i * 17
    box(ax, cols[0] - 8, y - 5, 16, 10, 'sujet', label=s)
    box(ax, cols[1] - 11, y - 5, 22, 10, 'varie', label=c)
    box(ax, cols[2] - 8, y - 5, 16, 10, 'resultat', label=v)
    arrow(ax, (cols[0] + 9, y), (cols[1] - 12, y), 'fixe'); arrow(ax, (cols[1] + 12, y), (cols[2] - 9, y), 'fixe')
arrow(ax, (3, 10), (3, 52), 'fixe', lw=1.0)
text(ax, 44, 3, 'on monte : 1, puis 2, puis 3', 'fixe', 's')
save(fig, '80-468')
