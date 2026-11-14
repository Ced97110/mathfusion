import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# ligne du haut : associés (vert) ; ligne du bas : pas associés (rouge)
text(ax, 44, 62, 'associés', 'resultat', 'm')
text(ax, 44, 26, 'pas associés', 'limite', 'm')
cells = [
    (42, 'resultat', 22, '3', '−3', 'unité\n× (−1)'),
    (42, 'resultat', 66, 'x + 1', '2x + 2', 'unité\n× 2'),
    (6, 'limite', 22, '3', '5', 'il faudrait\n5/3'),
    (6, 'limite', 66, 'x + 1', 'x + 2', 'pas une\nconstante'),
]
for y, role, cx, a, b, mid in cells:
    box(ax, cx - 21, y, 13, 14, role, label=a, size='s')
    box(ax, cx + 8, y, 13, 14, role, label=b, size='s')
    text(ax, cx - 0.5, y + 7, mid, role, 's')
save(fig, '56-039')
