import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes_xy(ax, ox, oy, u, nx, ny):
    arrow(ax, (ox - 2, oy), (ox + nx * u + 4, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy - 2), (ox, oy + ny * u + 4), "fixe", lw=0.8)
    for i in range(1, nx + 1): ax.plot([ox + i * u] * 2, [oy - 0.8, oy + 0.8], color=COL["fixe"], lw=0.6, zorder=1.5)
    for j in range(1, ny + 1): ax.plot([ox - 0.8, ox + 0.8], [oy + j * u] * 2, color=COL["fixe"], lw=0.6, zorder=1.5)
    text(ax, ox + nx * u + 3, oy - 3, r"$x$", "fixe", "s"); text(ax, ox - 3.5, oy + ny * u + 3, r"$y$", "fixe", "s")

fig, ax = canvas(92)
ox, oy, u = 14, 8, 11
box(ax, 3, 78, 34, 9, 'sujet', label=r'$x+y=5$')
box(ax, 51, 78, 34, 9, 'autre', label=r'$2x+2y=10$')
arrow(ax, (37, 82.5), (51, 82.5), 'varie'); text(ax, 44, 87, r'$\times 2$', 'varie', 's')
axes_xy(ax, ox, oy, u, 5, 5)
P = [(ox, oy + 5 * u), (ox + 5 * u, oy)]
line(ax, P, 'autre', lw=2.8); line(ax, P, 'sujet', lw=0.9)
for k in range(1, 5): disc(ax, ox + k * u, oy + (5 - k) * u, 1.1, 'resultat')
text(ax, 70, 56, 'les deux droites', 'encre', 's'); text(ax, 70, 52, 'sont confondues', 'encre', 's')
text(ax, 38, 24, 'une infinité', 'resultat', 's'); text(ax, 38, 20, 'de solutions', 'resultat', 's')
save(fig, '24-032')
