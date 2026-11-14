import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 33, 67, 'deux listes de diviseurs', 'fixe', 's')
for (L, ws, y, role) in (('q', (22, 12, 24), 48, 'sujet'), ('t', (18, 30, 10), 26, 'autre')):
    x = 4
    for i, w in enumerate(ws):
        box(ax, x, y, w - 1, 10, role, label=rf'${L}_{i+1}$')
        x += w
line(ax, [(62.5, 25), (62.5, 59)], 'fixe', lw=0.6, dash=True)
brace(ax, 4, 62, 24, 'fixe', label='n = somme des degrés')
text(ax, 76, 53, 'mêmes f, m', 'resultat', 's')
text(ax, 76, 34, 'n minimal ?', 'varie', 's')
save(fig, '60-271')
