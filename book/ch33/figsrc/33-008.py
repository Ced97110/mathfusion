import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for y, a, b, fw, bw in ((36, '5', '15', '×3', '÷3'), (8, '4', '16', 'carré', 'racine')):
    box(ax, 4, y, 16, 10, 'sujet', label=a)
    box(ax, 36, y, 16, 10, 'autre', label=b)
    box(ax, 68, y, 16, 10, 'resultat', label=a)
    arrow(ax, (21, y + 5), (35, y + 5), 'fixe')
    arrow(ax, (53, y + 5), (67, y + 5), 'varie')
    text(ax, 28, y + 9, fw, 'fixe', 's')
    text(ax, 60, y + 9, bw, 'varie', 's')
    text(ax, 44, y + 18, 'on retrouve le départ', 'resultat', 's')
    line(ax, [(12, y + 11.5), (12, y + 14.5), (76, y + 14.5), (76, y + 11.5)], 'resultat', dash=True)
save(fig, '33-008')
