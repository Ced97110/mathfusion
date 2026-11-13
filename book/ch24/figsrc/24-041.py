import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes_xy(ax, ox, oy, u, nx, ny):
    arrow(ax, (ox - 2, oy), (ox + nx * u + 4, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy - 2), (ox, oy + ny * u + 4), "fixe", lw=0.8)
    for i in range(1, nx + 1): ax.plot([ox + i * u] * 2, [oy - 0.8, oy + 0.8], color=COL["fixe"], lw=0.6, zorder=1.5)
    for j in range(1, ny + 1): ax.plot([ox - 0.8, ox + 0.8], [oy + j * u] * 2, color=COL["fixe"], lw=0.6, zorder=1.5)
    text(ax, ox + nx * u + 3, oy - 3, r"$x$", "fixe", "s"); text(ax, ox - 3.5, oy + ny * u + 3, r"$y$", "fixe", "s")

fig, ax = canvas(88)
ox, oy, u = 12, 8, 8
axes_xy(ax, ox, oy, u, 5, 8)
p = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [p(0, 5), p(5, 0)], 'sujet', lw=1.1); line(ax, [p(0, 8), p(4, 0)], 'autre', lw=1.1)
text(ax, p(0.5, 4.5)[0] + 6, p(0.5, 4.5)[1] + 4, r'$D_1$', 'sujet', 's'); text(ax, p(1.5, 5)[0] - 6, p(1.5, 5)[1] + 4, r'$D_2$', 'autre', 's')
line(ax, [p(3, 0), p(3, 7.2)], 'resultat', lw=1.4); text(ax, p(3, 7.2)[0], p(3, 7.2)[1] + 3, r'$x=3$', 'resultat', 's')
line(ax, [p(4, 0), p(4, 7.2)], 'fixe', dash=True); text(ax, p(4, 7.2)[0] + 1, p(4, 7.2)[1] + 3, r'$x=4$', 'fixe', 's')
disc(ax, *p(3, 2), 1.4, 'resultat'); text(ax, p(3, 2)[0] + 3, p(3, 2)[1] + 3, r'$P$', 'resultat', 's')
text(ax, p(3, 2)[0] - 3, p(3, 2)[1] - 3, '2', 'resultat', 's')
disc(ax, *p(4, 1), 1.1, 'sujet'); disc(ax, *p(4, 0), 1.1, 'autre')
text(ax, p(4, 1)[0] + 3, p(4, 1)[1] + 2.5, '1', 'sujet', 's')
text(ax, 74, 50, 'en x = 3 :', 'resultat', 's'); text(ax, 74, 46, 'même hauteur', 'resultat', 's')
text(ax, 74, 30, 'en x = 4 :', 'fixe', 's'); text(ax, 74, 26, 'hauteurs 1 et 0', 'fixe', 's')
save(fig, '24-041')
