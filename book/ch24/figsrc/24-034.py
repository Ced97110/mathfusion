import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes_xy(ax, ox, oy, u, nx, ny):
    arrow(ax, (ox - 2, oy), (ox + nx * u + 4, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy - 2), (ox, oy + ny * u + 4), "fixe", lw=0.8)
    for i in range(1, nx + 1): ax.plot([ox + i * u] * 2, [oy - 0.8, oy + 0.8], color=COL["fixe"], lw=0.6, zorder=1.5)
    for j in range(1, ny + 1): ax.plot([ox - 0.8, ox + 0.8], [oy + j * u] * 2, color=COL["fixe"], lw=0.6, zorder=1.5)
    text(ax, ox + nx * u + 3, oy - 3, r"$x$", "fixe", "s"); text(ax, ox - 3.5, oy + ny * u + 3, r"$y$", "fixe", "s")

fig, ax = canvas(68)
ox, oy, u = 10, 26, 10
axes_xy(ax, ox, oy, u, 6, 3)
p = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [p(3, -0.3), p(3, 3.4)], 'sujet', lw=1.4); line(ax, [p(5, -0.3), p(5, 3.4)], 'autre', lw=1.4)
disc(ax, *p(3, 0), 1.0, 'sujet'); disc(ax, *p(5, 0), 1.0, 'autre')
text(ax, p(3, 0)[0], 63, r'$x=3$', 'sujet', 'm'); text(ax, p(5, 0)[0], 63, r'$x=5$', 'autre', 'm')
text(ax, p(3, 0)[0] - 3.5, p(0, 0)[1] + 3, '3', 'sujet', 's'); text(ax, p(5, 0)[0] + 3.5, p(0, 0)[1] + 3, '5', 'autre', 's')
text(ax, p(3, 0)[0] - 2, p(0, 2)[1], 'pente : aucune', 'sujet', 's', ha='right')
text(ax, p(5, 0)[0] + 2, p(0, 2)[1], 'pente : aucune', 'autre', 's', ha='left')
text(ax, 44, 17, 'aucun point commun', 'encre', 's')
box(ax, 14, 2, 60, 11, 'fixe', label="critère des pentes :\nne s'applique pas")
save(fig, '24-034')
