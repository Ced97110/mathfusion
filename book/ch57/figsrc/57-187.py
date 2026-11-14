import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, s = 5, 10, 6.5
P = lambda x, y: (ox + x * s, oy + y * s)
# classes : x - 2y = c  ->  y = (x - c) / 2
cls = [(0, 'sujet', [(0, 0), (2, 1), (4, 2), (6, 3)]),
       (1, 'varie', [(1, 0), (3, 1), (5, 2)]),
       (-1, 'autre', [(1, 1), (3, 2), (5, 3)])]
for c, r, pts in cls:
    x0 = max(0, c); y0 = (x0 - c) / 2
    x1 = min(6, 6 + c); y1 = (x1 - c) / 2
    line(ax, [P(x0, y0), P(x1, y1)], r, lw=1.1)
    for (x, y) in pts: disc(ax, P(x, y)[0], P(x, y)[1], 1.5, r)
text(ax, 25, 54, r'classes de $\mathbb{Z}^2/N$', 'encre', 's')
text(ax, 47, 33, '≅', 'encre', 'xl', weight='bold')
f = numberline(ax, 56, 80, 33, -2, 2, arrow_right=False)
for c, r, _ in cls:
    disc(ax, f(c), 33, 2.0, r)
text(ax, 68, 46, 'repères', 'encre', 's')
text(ax, 68, 41, r'dans $\mathbb{Z}$', 'encre', 's')
text(ax, 44, 4, 'une classe ↔ un entier', 'resultat', 'm')
save(fig, '57-187')
