import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, s, nx, ny, xl="x", yl="y"):
    arrow(ax, (ox - 1, oy), (ox + nx * s + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy - 1), (ox, oy + ny * s + 3), "fixe", lw=0.8)
    for i in range(1, nx + 1): line(ax, [(ox + i * s, oy - 0.8), (ox + i * s, oy + 0.8)], "fixe", lw=0.6)
    for j in range(1, ny + 1): line(ax, [(ox - 0.8, oy + j * s), (ox + 0.8, oy + j * s)], "fixe", lw=0.6)
    text(ax, ox + nx * s + 5, oy - 2.5, "$" + xl + "$", "fixe", "s"); text(ax, ox - 3, oy + ny * s + 4, "$" + yl + "$", "fixe", "s")
    return lambda X, Y: (ox + X * s, oy + Y * s)

fig, ax = canvas(80)
P = axes(ax, 14, 8, 8, 4, 6)
line(ax, [P(0, 1), P(2.5, 6)], 'fixe', lw=1.2)
line(ax, [P(1, 3), P(2, 3)], 'varie', lw=1.6); line(ax, [P(2, 3), P(2, 5)], 'sujet', lw=1.6)
for X in (1, 2): disc(ax, *P(X, 1 + 2 * X), 1.1, 'fixe')
text(ax, P(1.5, 3)[0], P(1.5, 3)[1] - 3, '+1', 'varie', 'm')
text(ax, P(2, 4)[0] + 6, P(2, 4)[1], r'$+2=m$', 'sujet', 'l')
text(ax, 62, 70, r'$y=2x+1$', 'encre', 'l')
text(ax, 62, 62, r'$m=2$', 'sujet', 'l')
save(fig, '19-084')
