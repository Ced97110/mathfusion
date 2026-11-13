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
line(ax, [p(3, 0), p(3, 7.6)], 'sujet', lw=1.5); text(ax, p(3, 7.6)[0], p(3, 7.6)[1] + 3, r'$x=3$', 'sujet', 'm')
for y in (0, 2, 7):
    disc(ax, *p(3, y), 1.3, 'resultat')
    text(ax, p(3, y)[0] + 3, p(3, y)[1] + (3 if y == 0 else 0), f'$(3,\\ {y})$', 'resultat', 's', ha='left')
text(ax, 70, 40, 'tous les points', 'sujet', 's'); text(ax, 70, 36, 'd’abscisse 3', 'sujet', 's')
text(ax, 70, 30, '$y$ : au choix', 'encre', 's')
save(fig, '24-042')
