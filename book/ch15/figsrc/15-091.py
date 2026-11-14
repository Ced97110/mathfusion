import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [('$x$', '$x$', '$x^2$'), ('$x$', '$3$', '$3x$'), ('$2$', '$x$', '$2x$'), ('$2$', '$3$', '$6$')]
ys = [56, 44, 32, 20]
for y, (p, q, r) in zip(ys, rows):
    box(ax, 4, y, 14, 9, 'sujet', label=p)
    box(ax, 22, y, 14, 9, 'autre', label=q)
    arrow(ax, (38, y + 4.5), (47, y + 4.5), 'varie')
    box(ax, 49, y, 22, 9, 'varie', label=r)
line(ax, [(73, ys[1] + 4.5), (76, ys[1] + 4.5), (76, ys[2] + 4.5), (73, ys[2] + 4.5)], 'varie')
text(ax, 81, (ys[1] + ys[2]) / 2 + 4.5, '$5x$', 'resultat', 'm')
arrow(ax, (60, 19), (60, 13), 'resultat')
text(ax, 60, 8, r'$x^2 + 5x + 6$', 'resultat', 'l')
save(fig, '15-091')
