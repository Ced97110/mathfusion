import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
f = numberline(ax, 6, 60, 58, 0, 6, every=3)
text(ax, 72, 58, 'rail', 'fixe', 's')
disc(ax, f(3), 61.5, 2.2, 'sujet')
arrow(ax, (f(3) + 2.4, 61.5), (f(5), 61.5), 'varie')
text(ax, 44, 67, r'$v$ = 2 m/s', 'varie', 's')
brace(ax, f(0), f(3), 66, 'sujet', r'$x$ = 3 m', down=False)
ox, oy, u = 14, 8, 9
arrow(ax, (ox, oy), (ox + 6 * u + 4, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy), (ox, oy + 3 * u + 4), 'fixe', lw=0.8)
text(ax, ox + 6 * u + 4, oy - 3, r'$x$', 'fixe', 's'); text(ax, ox - 4, oy + 3 * u + 4, r'$v$', 'fixe', 's')
px, py = ox + 3 * u, oy + 2 * u
line(ax, [(px, oy), (px, py)], 'fixe', dash=True); line(ax, [(ox, py), (px, py)], 'fixe', dash=True)
disc(ax, px, py, 1.8, 'sujet')
text(ax, px, oy - 3, '3', 'sujet', 's'); text(ax, ox - 3, py, '2', 'varie', 's')
text(ax, px + 3, py + 4, '(3, 2)', 'sujet', 's', ha='left')
save(fig, '75-001')
