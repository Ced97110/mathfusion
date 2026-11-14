import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle as R
fig, ax = canvas(88)
s, ox, oy = 11.0, 8, 10
nx, ny = 6, 6
P = lambda x, y: (ox + x * s, oy + y * s)
clip = R((ox - 1, oy - 1), nx * s + 2, ny * s + 2, transform=ax.transData)
for u in range(-6, 8):  # droites u = const, direction e'2 = (1,1)
    a, b = P(2 * u - 20, 3 * u - 20), P(2 * u + 20, 3 * u + 20)
    l, = ax.plot([a[0], b[0]], [a[1], b[1]], color=COL['fixe'], lw=0.5, zorder=1); l.set_clip_path(clip)
for v in range(-6, 8):  # droites v = const, direction e'1 = (2,3)
    a, b = P(v - 20, v - 30), P(v + 20, v + 30)
    l, = ax.plot([a[0], b[0]], [a[1], b[1]], color=COL['fixe'], lw=0.5, zorder=1); l.set_clip_path(clip)
for i in range(nx + 1):
    for j in range(ny + 1):
        ax.plot([P(i, j)[0]], [P(i, j)[1]], 'o', color=COL['fixe'], ms=2.6, zorder=2)
poly(ax, [P(0, 0), P(2, 3), P(3, 4), P(1, 1)], 'varie')
arrow(ax, P(0, 0), P(2, 3), 'varie', lw=1.5)
arrow(ax, P(0, 0), P(1, 1), 'varie', lw=1.5)
disc(ax, *P(1, 0), 1.5, 'resultat'); disc(ax, *P(0, 1), 1.5, 'resultat')
text(ax, P(2, 3)[0] + 9, P(2, 3)[1] + 1, r"$e'_1=(2,\,3)$", 'varie', 's')
text(ax, P(1, 1)[0] + 11, P(1, 1)[1] - 4, r"$e'_2=(1,\,1)$", 'varie', 's')
text(ax, P(1, 0)[0] + 4, P(1, 0)[1] - 3, r'$e_1$', 'resultat', 's')
text(ax, P(0, 1)[0] - 4, P(0, 1)[1] + 3, r'$e_2$', 'resultat', 's')
text(ax, 44, 3.5, 'chaque point : une seule écriture', 'fixe', 's')
save(fig, '59-019')
