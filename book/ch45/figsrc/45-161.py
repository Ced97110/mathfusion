import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 53, 56, 'case G', 'sujet', 'm'); text(ax, 74, 56, 'case H', 'autre', 'm')
for y, lab in zip([42, 30, 18], ['neutre (0, 0)', 'inverse (1, 1)', 'associativité']):
    box(ax, 3, y - 4.5, 34, 9, 'fixe', label=lab)
    box(ax, 44, y - 4.5, 18, 9, 'sujet', label='✓'); box(ax, 65, y - 4.5, 18, 9, 'autre', label='✓')
    arrow(ax, (37.5, y), (43.5, y), 'varie')
box(ax, 3, 2, 80, 9, 'resultat', label=r'$G\times H$ est un groupe')
save(fig, '45-161')
