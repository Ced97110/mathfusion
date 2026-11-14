import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 8
text(ax, 20, 60, r'$\frac{3}{4}$', 'encre', 'l'); text(ax, 62, 60, r'$-\frac{1}{2}$', 'encre', 'l')
ox, oy = 4, 14
arrow(ax, (ox, oy), (ox + 4 * u, oy), 'varie'); arrow(ax, (ox + 4 * u, oy), (ox + 4 * u, oy + 3 * u), 'sujet')
disc(ax, ox, oy, 1.3, 'fixe')
text(ax, ox + 2 * u, oy - 3.5, '+4', 'varie', 's'); text(ax, ox + 4 * u - 3, oy + 1.5 * u, '+3', 'sujet', 's', ha='right')
px, py = 48, 38
arrow(ax, (px, py), (px + 2 * u, py), 'varie'); arrow(ax, (px + 2 * u, py), (px + 2 * u, py - u), 'sujet')
disc(ax, px, py, 1.3, 'fixe')
text(ax, px + u, py + 3.5, '+2', 'varie', 's'); text(ax, px + 2 * u + 3, py - u / 2, '−1', 'sujet', 's', ha='left')
text(ax, 44, 4, 'même méthode : seul le signe change', 'fixe', 's')
save(fig, '19-095')
