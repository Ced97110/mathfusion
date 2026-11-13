import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 64, 'modules 2 et 4', 'limite', 'm')
text(ax, 66, 64, 'modules 3, 4, 5', 'resultat', 'm')
line(ax, [(44, 10), (44, 60)], 'fixe', dash=True)
for y, n, role in [(44, '0', 'sujet'), (22, '4', 'autre')]:
    box(ax, 4, y, 8, 8, role, label=n)
box(ax, 24, 30, 17, 8, 'limite', label='(0, 0)')
arrow(ax, (13, 48), (24, 36), 'varie')
arrow(ax, (13, 26), (24, 32), 'varie')
text(ax, 32, 24, 'même liste', 'limite', 's')
for y, n, lst, role in [(44, '7', '(1, 3, 2)', 'sujet'), (22, '8', '(2, 0, 3)', 'autre')]:
    box(ax, 48, y, 8, 8, role, label=n)
    arrow(ax, (57, y + 4), (60, y + 4), 'varie')
    box(ax, 61, y, 25, 8, role, label=lst)
text(ax, 66, 14, 'listes différentes', 'resultat', 's')
save(fig, '52-241')
