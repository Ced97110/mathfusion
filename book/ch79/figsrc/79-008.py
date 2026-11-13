import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, 'deux chemins, 4 étapes chacun', 'encre', 'm')
y0, dy = 14, 12
A = [(44, y0, '1'), (16, y0 + dy, '2'), (16, y0 + 2 * dy, '4'), (16, y0 + 3 * dy, '12'), (44, y0 + 4 * dy, '60')]
B = [(44, y0, '1'), (72, y0 + dy, '5'), (72, y0 + 2 * dy, '15'), (72, y0 + 3 * dy, '30'), (44, y0 + 4 * dy, '60')]
r = 3.6
for path, role in ((A, 'varie'), (B, 'autre')):
    for (x1, y1, _), (x2, y2, _) in zip(path, path[1:]):
        d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
        arrow(ax, (x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r), role, lw=1.2)
for x, y, s in A[1:4]: disc(ax, x, y, r, 'varie', label=s, size='s')
for x, y, s in B[1:4]: disc(ax, x, y, r, 'autre', label=s, size='s')
disc(ax, 44, y0, r, 'sujet', label='1', size='s'); disc(ax, 44, y0 + 4 * dy, r, 'resultat', label='60', size='s')
text(ax, 20, 5, '×2, ×2, ×3, ×5', 'varie', 's'); text(ax, 68, 5, '×5, ×3, ×2, ×2', 'autre', 's')
save(fig, '79-008')
