import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
y = lambda v: 14 + (v + 2) * 8
line(ax, [(24, y(-2)), (24, y(3))], 'fixe')
labs = {3: '3', 2: '2', 1: '1', 0: '0', -1: '1', -2: '2'}
for v, s in labs.items():
    line(ax, [(22.8, y(v)), (25.2, y(v))], 'fixe')
    text(ax, 19, y(v), s, 'fixe', 's')
line(ax, [(27, y(0)), (50, y(0))], 'fixe', dash=True)
text(ax, 36, y(0) + 2.4, '0', 'encre', 's')
# the same number 2, on the other side
disc(ax, 24, y(2), 1.8, 'autre', fill=False)
text(ax, 8, y(2), 'au-dessus', 'autre', 's')
text(ax, 8, y(-2), 'sous zéro', 'resultat', 's')
text(ax, 27.5, y(2), '2 seul : quel côté ?', 'autre', 's', ha='left')
disc(ax, 24, y(3), 1.8, 'sujet'); text(ax, 24, y(3) + 4.5, 'départ : 3 degrés', 'sujet', 'm')
arrow(ax, (52, y(3)), (52, y(0)), 'varie'); text(ax, 56, y(1.5), 'baisse de 3', 'varie', 'm', ha='left')
arrow(ax, (52, y(0)), (52, y(-2)), 'varie'); text(ax, 56, y(-1), 'baisse de 2', 'varie', 'm', ha='left')
disc(ax, 24, y(-2), 1.8, 'resultat'); text(ax, 24, y(-2) - 5, '2 degrés sous zéro', 'resultat', 'm')
save(fig, '13-003')
