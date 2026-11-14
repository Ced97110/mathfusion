import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 2, 6, 11
m = lambda x, y: (ox + (x + 1) * u, oy + (y + 1) * u)
poly(ax, [m(-1, -1), m(6, -1), m(6, 4), m(-1, 4)], 'fixe', fill=False)
line(ax, [m(-1, 0), m(6, 0)], 'fixe'); line(ax, [m(0, -1), m(0, 4)], 'fixe')
poly(ax, [m(-1, -1), m(-1, 0), m(1, 2), m(4, -1)], 'resultat')
line(ax, [m(-1, 0), m(3, 4)], 'varie', lw=1.3)
line(ax, [m(-1, 4), m(4, -1)], 'sujet', lw=1.3)
c = m(1, 1); disc(ax, c[0], c[1], 1.3, 'resultat')
text(ax, c[0] + 2.2, c[1] - 3.2, r'$(1,\,1)$', 'resultat', 's', ha='left')
c = m(5, 0); disc(ax, c[0], c[1], 1.3, 'limite')
text(ax, c[0], c[1] + 4, r'$(5,\,0)$', 'limite', 's')
rows = [('varie', r'$y\leq x+1$'), ('sujet', r'$x+y\leq 3$')]
for i, (r, t) in enumerate(rows):
    p = m(3.45, 3.6 - i * 0.8)
    line(ax, [p, (p[0] + 4, p[1])], r, lw=1.3); text(ax, p[0] + 5.5, p[1], t, r, 's', ha='left')
text(ax, *m(0.1, -0.55), 'région commune', 'resultat', 's', ha='left')
save(fig, '20-109')
