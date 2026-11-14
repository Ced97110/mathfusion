import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xl, xr = 14, 40
ys = lambda s: 30 + 20 * s
line(ax, [(xl, 10), (xl, 50)], 'fixe')
line(ax, [(xr, 10), (xr, 50)], 'sujet', lw=1.4)
for s, a, b in [(1, '1', '4 m'), (0, '0', '2 m (milieu)'), (-1, '−1', '0 m')]:
    y = ys(s)
    line(ax, [(xl - 1, y), (xl + 1, y)], 'fixe')
    line(ax, [(xr - 1, y), (xr + 1, y)], 'sujet')
    text(ax, xl - 2.5, y, a, 'fixe', 'm', ha='right')
    text(ax, xr + 2.5, y, b, 'sujet', 'm', ha='left')
    arrow(ax, (xl + 2, y), (xr - 2, y), 'varie')
text(ax, 27, 34, r'$\times 2$ puis $+2$', 'varie', 's')
text(ax, xl, 55, 'sinus', 'fixe', 'm')
text(ax, xr, 55, 'hauteur', 'sujet', 'm')
arrow(ax, (63, 31.5), (63, 49), 'varie')
arrow(ax, (63, 28.5), (63, 11), 'varie')
text(ax, 77, 40, 'écart 2', 'varie', 's')
text(ax, 77, 20, 'écart 2', 'varie', 's')
save(fig, '32-004')
