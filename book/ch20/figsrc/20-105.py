import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 4, 8, 10
m = lambda x, y: (ox + (x + 1) * u, oy + (y + 1) * u)
poly(ax, [m(-1, -1), m(7, -1), m(7, 5), m(-1, 5)], 'fixe', fill=False)
poly(ax, [m(0, 0), m(6, 0), m(0, 4)], 'resultat')
line(ax, [m(-1, 14 / 3), m(7, -2 / 3)], 'sujet', lw=1.4)
line(ax, [m(0, -1), m(0, 5)], 'varie', lw=1.4)
line(ax, [m(-1, 0), m(7, 0)], 'autre', lw=1.4)
for p in [(0, 0), (6, 0), (0, 4)]:
    c = m(*p); disc(ax, c[0], c[1], 1.3, 'resultat')
text(ax, *m(0.3, -0.55), r'$(0,\,0)$', 'resultat', 's', ha='left')
text(ax, *m(6, -0.55), r'$(6,\,0)$', 'resultat', 's')
text(ax, *m(0.35, 4.35), r'$(0,\,4)$', 'resultat', 's', ha='left')
text(ax, *m(4.3, 2.6), r'$2x+3y\leq 12$', 'sujet', 's', ha='left')
text(ax, *m(0.3, 4.75), r'$x\geq 0$', 'varie', 's', ha='left')
text(ax, *m(6.9, 0.5), r'$y\geq 0$', 'autre', 's', ha='right')
text(ax, *m(2.0, 0.9), 'triangle', 'resultat', 's')
save(fig, '20-105')
