import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 58, 72, 'horloges 3 · 4 · 5', 'fixe', 's')
cols = [42, 58, 74]
rows = [(56, r'$7\times8$', [2, 0, 1], 'sujet'), (40, r'$+\,3$', [0, 3, 3], 'autre'), (24, 'somme', [2, 3, 4], 'varie')]
for y, lab, vals, role in rows:
    text(ax, 3, y + 4.5, lab, 'encre', 'm', ha='left')
    for c, v in zip(cols, vals):
        box(ax, c - 6, y, 12, 9, role, label=str(v))
arrow(ax, (58, 24), (58, 15.5), 'fixe')
box(ax, 36, 3, 44, 11, 'resultat', label='recollé : 59', size='l')
save(fig, '52-262')
