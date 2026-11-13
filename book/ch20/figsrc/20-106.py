import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ox, oy, u = 4, 8, 10
m = lambda x, y: (ox + (x + 1) * u, oy + (y + 1) * u)
poly(ax, [m(-1, -1), m(7, -1), m(7, 5), m(-1, 5)], 'fixe', fill=False)
poly(ax, [m(0, 0), m(6, 0), m(0, 4)], 'sujet')
pts = [((0, 0), 'sujet', r'$(0,\,0)$ : 0', (0.35, -0.55), 'left'),
       ((6, 0), 'sujet', r'$(6,\,0)$ : 6', (6, -0.6), 'center'),
       ((0, 4), 'resultat', r'$(0,\,4)$ : 8', (0.4, 4.0), 'left'),
       ((3, 2), 'varie', r'$(3,\,2)$ : 7', (3.4, 2.5), 'left')]
for p, r, t, tp, ha in pts:
    c = m(*p); disc(ax, c[0], c[1], 1.3, r)
    text(ax, *m(*tp), t, r, 's', ha=ha, weight='bold' if r == 'resultat' else 'normal')
text(ax, *m(3.0, 4.6), r'plaisir $=x+2y$', 'encre', 's')
text(ax, *m(5.0, 1.3), 'côté : 6, 7, 8', 'varie', 's')
save(fig, '20-106')
