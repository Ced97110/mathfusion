import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes_xy(ax, ox, oy, u, nx, ny):
    arrow(ax, (ox - 2, oy), (ox + nx * u + 4, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy - 2), (ox, oy + ny * u + 4), "fixe", lw=0.8)
    for i in range(1, nx + 1): ax.plot([ox + i * u] * 2, [oy - 0.8, oy + 0.8], color=COL["fixe"], lw=0.6, zorder=1.5)
    for j in range(1, ny + 1): ax.plot([ox - 0.8, ox + 0.8], [oy + j * u] * 2, color=COL["fixe"], lw=0.6, zorder=1.5)
    text(ax, ox + nx * u + 3, oy - 3, r"$x$", "fixe", "s"); text(ax, ox - 3.5, oy + ny * u + 3, r"$y$", "fixe", "s")

fig, ax = canvas(84)
ox, oy, u = 14, 8, 8
axes_xy(ax, ox, oy, u, 5, 8)
p = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [p(0, 5), p(5, 0)], 'sujet', lw=1.1); line(ax, [p(0, 8), p(4, 0)], 'autre', lw=1.1)
for (a, b) in [(0, 5), (1, 4), (5, 0)]: disc(ax, *p(a, b), 1.0, 'sujet')
line(ax, [p(3, 0), p(3, 2)], 'fixe', dash=True); line(ax, [p(0, 2), p(3, 2)], 'fixe', dash=True)
disc(ax, *p(3, 2), 1.5, 'resultat')
text(ax, p(3, 0)[0], oy - 4, '3', 'resultat', 's'); text(ax, ox - 4, p(0, 2)[1], '2', 'resultat', 's')
box(ax, 62, 56, 22, 8, 'resultat', label=r'$(3,\ 2)$'); arrow(ax, (62, 58), (p(3, 2)[0] + 1.8, p(3, 2)[1] + 0.8), 'resultat')
text(ax, 74, 42, 'ticket du lundi', 'sujet', 's'); text(ax, 74, 36, 'ticket du mardi', 'autre', 's')
text(ax, 74, 26, 'le croisement', 'resultat', 's'); text(ax, 74, 22, 'donne la réponse', 'resultat', 's')
save(fig, '24-035')
