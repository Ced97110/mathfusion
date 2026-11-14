import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
ox, oy, u = 2, 4, 8.8
m = lambda x, y: (ox + (x + 2) * u, oy + (y + 2) * u)
poly(ax, [m(-2, -1), m(3, 4), m(-2, 4)], 'varie')
poly(ax, [m(-1, -2), m(4, 3), m(4, -2)], 'sujet')
poly(ax, [m(-2, -2), m(4, -2), m(4, 4), m(-2, 4)], 'fixe', fill=False)
line(ax, [m(-2, -1), m(3, 4)], 'varie', lw=1.3, dash=True)
line(ax, [m(-1, -2), m(4, 3)], 'sujet', lw=1.3, dash=True)
c = m(0, 3); disc(ax, c[0], c[1], 1.3, 'varie')
text(ax, c[0] + 2.2, c[1], r'$(0,\,3)$', 'varie', 's', ha='left')
rows = [('varie', r'$y>x+1$'), ('sujet', r'$y<x-1$')]
for i, (r, t) in enumerate(rows):
    y = 50 - i * 9
    line(ax, [(57, y), (61, y)], r, lw=1.3, dash=True); text(ax, 62.5, y, t, r, 's', ha='left')
text(ax, 71, 28, 'zone commune :', 'limite', 's')
text(ax, 71, 24, 'aucune', 'limite', 's', weight='bold')
text(ax, 71, 12, 'pente 1 :', 'fixe', 's')
text(ax, 71, 8, 'parallèles', 'fixe', 's')
save(fig, '20-111')
