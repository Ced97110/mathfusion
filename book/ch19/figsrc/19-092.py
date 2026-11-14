import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, s, nx, ny, xl="x", yl="y"):
    arrow(ax, (ox - 1, oy), (ox + nx * s + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy - 1), (ox, oy + ny * s + 3), "fixe", lw=0.8)
    for i in range(1, nx + 1): line(ax, [(ox + i * s, oy - 0.8), (ox + i * s, oy + 0.8)], "fixe", lw=0.6)
    for j in range(1, ny + 1): line(ax, [(ox - 0.8, oy + j * s), (ox + 0.8, oy + j * s)], "fixe", lw=0.6)
    text(ax, ox + nx * s + 5, oy - 2.5, "$" + xl + "$", "fixe", "s"); text(ax, ox - 3, oy + ny * s + 4, "$" + yl + "$", "fixe", "s")
    return lambda X, Y: (ox + X * s, oy + Y * s)

fig, ax = canvas(72)
P = axes(ax, 8, 8, 6, 3, 6); Q = axes(ax, 50, 8, 6, 4, 6)
line(ax, [P(0, 1), P(2.5, 6)], 'resultat', lw=1.4)
line(ax, [Q(4, 0), Q(4, 6)], 'limite', lw=1.4)
text(ax, 24, 64, 'pente et départ lus', 'resultat', 's'); text(ax, 66, 64, 'rien à lire', 'limite', 's')
text(ax, 24, 56, r'$y=2x+1$', 'resultat', 'm'); text(ax, 70, 56, r'$x=4$', 'limite', 'm')
save(fig, '19-092')
