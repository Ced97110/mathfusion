import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
rows = [(30, 'Lagrange', 'sujet', ['5', '16/5']), (8, 'matrice $P$', 'autre', ['16', '4'])]
for y, lab, role, vals in rows:
    text(ax, 2, y + 5, lab, role, 's', ha='left')
    for i, v in enumerate(vals):
        box(ax, 22 + i * 19, y, 16, 10, role, label=v, size='m')
        arrow(ax, (22 + i * 19 + 16, y + 5), (62, 22 + (y - 19) * 0.25), 'fixe', lw=0.6) if False else None
    arrow(ax, (59, y + 5), (66, 24 + (y - 19) * 0.2), 'resultat', lw=0.9)
box(ax, 66, 14, 20, 20, 'resultat', label='+   +', size='l', weight='bold')
text(ax, 76, 38, 'mêmes signes', 'resultat', 's')
text(ax, 40, 22, 'nombres différents', 'varie', 's')
save(fig, '71-177')
