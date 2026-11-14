import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
M = lambda ox, oy, u: (lambda x, y: (ox + (x + 1) * u, oy + (y + 1) * u))
HP = {'sujet': [(-1, -1), (7, -1), (7, -2 / 3), (-1, 14 / 3)],
      'varie': [(0, -1), (7, -1), (7, 5), (0, 5)],
      'autre': [(-1, 0), (7, 0), (7, 5), (-1, 5)]}
names = {'sujet': r'budget', 'varie': r'$x\geq 0$', 'autre': r'$y\geq 0$'}
for i, r in enumerate(['sujet', 'varie', 'autre']):
    m = M(2 + i * 29, 62, 3)
    poly(ax, [m(*p) for p in HP[r]], r)
    poly(ax, [m(-1, -1), m(7, -1), m(7, 5), m(-1, 5)], 'fixe', fill=False)
    text(ax, 2 + i * 29 + 12, 84, names[r], r, 's')
m = M(3, 4, 8)
poly(ax, [m(-1, -1), m(7, -1), m(7, 5), m(-1, 5)], 'fixe', fill=False)
poly(ax, [m(0, 0), m(6, 0), m(0, 4)], 'resultat')
line(ax, [m(-1, 14 / 3), m(7, -2 / 3)], 'sujet', lw=1.2)
line(ax, [m(0, -1), m(0, 5)], 'varie', lw=1.2)
line(ax, [m(-1, 0), m(7, 0)], 'autre', lw=1.2)
text(ax, 77, 40, 'zone commune', 'resultat', 's')
arrow(ax, (70, 37), m(1.6, 1), 'resultat')
text(ax, 44, 57, 'dans les trois à la fois', 'encre', 's')
save(fig, '20-099')
