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
line(ax, [p(0, 5), p(5, 0)], 'sujet', lw=1.2); line(ax, [p(0, 8), p(4, 0)], 'autre', lw=1.2)
for y0, drop, role in [(5, 1, 'sujet'), (8, 2, 'autre')]:
    line(ax, [p(0, y0), p(1, y0)], 'varie', lw=1.2); line(ax, [p(1, y0), p(1, y0 - drop)], role, lw=1.2, dash=True)
    text(ax, p(0.5, y0)[0], p(0.5, y0)[1] + 2.5, r'$+1$', 'varie', 's')
    text(ax, p(1, y0 - drop / 2)[0] + 4, p(1, y0 - drop / 2)[1], f'$-{drop}$', role, 's')
disc(ax, *p(3, 2), 1.3, 'resultat')
box(ax, 62, 62, 24, 8, 'sujet', label=r'$y=5-x$'); text(ax, 74, 57, 'pente $-1$', 'sujet', 's')
box(ax, 62, 42, 24, 8, 'autre', label=r'$y=8-2x$'); text(ax, 74, 37, 'pente $-2$', 'autre', 's')
text(ax, 74, 24, 'pentes différentes :', 'resultat', 's'); text(ax, 74, 20, 'elles se croisent', 'resultat', 's')
save(fig, '24-033')
