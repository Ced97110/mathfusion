import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ox, oy = 22, 38
X = lambda x: ox + 12 * x
Yv = lambda y: oy + 8 * y
arrow(ax, (ox - 8, oy), (X(3.2), oy), 'fixe', lw=0.6)
xs = [0.5 + i * 0.025 for i in range(101)]
line(ax, [(X(x), Yv(1 / x)) for x in xs], 'sujet', lw=1.3)
line(ax, [(X(x), Yv(2 / x)) for x in xs], 'autre', lw=1.3)
line(ax, [(ox, oy - 2), (ox, Yv(4.4))], 'varie', lw=1.3, dash=True)
text(ax, ox + 2, Yv(4.4) + 1, r'$x=0$', 'varie', 's', ha='left')
text(ax, X(3.0) + 1.5, Yv(1 / 3.0) - 1.0, r'$xy=1$', 'sujet', 's', ha='left')
text(ax, X(3.0) + 1.5, Yv(2 / 3.0) + 2.0, r'$xy=2$', 'autre', 's', ha='left')
text(ax, 66, 66, 'aucun point\ncommun', 'limite', 's')
# number line of x : root of -x
f = numberline(ax, 10, 58, 14, -1, 3, 1, arrow_right=False)
disc(ax, f(0), 14, 1.4, 'varie')
text(ax, f(0), 21, r'$-x=0$ en $x=0$', 'varie', 's')
text(ax, 72, 14, 'têtes :\n0 et 0', 'varie', 's')
save(fig, '70-123')
