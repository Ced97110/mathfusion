import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, s, nx, ny, xl="x", yl="y"):
    arrow(ax, (ox - 1, oy), (ox + nx * s + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy - 1), (ox, oy + ny * s + 3), "fixe", lw=0.8)
    for i in range(1, nx + 1): line(ax, [(ox + i * s, oy - 0.8), (ox + i * s, oy + 0.8)], "fixe", lw=0.6)
    for j in range(1, ny + 1): line(ax, [(ox - 0.8, oy + j * s), (ox + 0.8, oy + j * s)], "fixe", lw=0.6)
    text(ax, ox + nx * s + 5, oy - 2.5, "$" + xl + "$", "fixe", "s"); text(ax, ox - 3, oy + ny * s + 4, "$" + yl + "$", "fixe", "s")
    return lambda X, Y: (ox + X * s, oy + Y * s)

fig, ax = canvas(72)
P = axes(ax, 10, 10, 14, 4, 3)
line(ax, [P(0, 2), P(4, 0)], 'fixe', lw=1.2)
line(ax, [P(0, 2), P(2, 2)], 'varie', lw=1.6); line(ax, [P(2, 2), P(2, 1)], 'sujet', lw=1.6)
disc(ax, *P(0, 2), 1.5, 'autre'); disc(ax, *P(2, 1), 1.5, 'resultat')
text(ax, P(0, 2)[0] + 2, P(0, 2)[1] + 8, r'$(0,\ 2)$', 'autre', 's', ha='left')
text(ax, P(2, 1)[0] - 2, P(2, 1)[1] - 4, r'$(2,\ 1)$', 'resultat', 's', ha='right')
text(ax, P(1.45, 2)[0], P(1.45, 2)[1] + 4, 'avancer de 2', 'varie', 's'); text(ax, P(2, 1.5)[0] + 3, P(2, 1.5)[1], 'descendre de 1', 'sujet', 's', ha='left')
text(ax, 68, 64, r'$-\frac{1}{2}=\frac{-1}{2}$', 'encre', 'l')
save(fig, '19-096')
