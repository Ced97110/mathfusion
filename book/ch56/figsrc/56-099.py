import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
vals = [48, 24, 12, 6, 3]
ys = [82 - 18 * i for i in range(5)]
for i, (v, y) in enumerate(zip(vals, ys)):
    box(ax, 8, y, 16, 9, 'resultat' if v == 3 else 'sujet', label=str(v), size='m')
for y0, y1 in zip(ys[:-1], ys[1:]):
    arrow(ax, (16, y0), (16, y1 + 9), 'fixe')
    text(ax, 28, (y0 + y1 + 9) / 2, '× 2', 'fixe', 's')
text(ax, 66, 96, '48 = 3 × 16', 'encre', 'l')
arrow(ax, (24.5, ys[0] + 4.5), (45.5, ys[0] + 4.5), 'varie')
box(ax, 46, ys[0], 40, 9, 'varie', label='reste 16 : nouvelle chaîne', size='s', dash=True)
box(ax, 46, ys[-1], 40, 9, 'resultat', label='3 irréductible : stop', size='s')
arrow(ax, (24, ys[-1] + 4.5), (46, ys[-1] + 4.5), 'resultat')
save(fig, '56-099')
