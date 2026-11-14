import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, s, nx, ny, xl="x", yl="y"):
    arrow(ax, (ox - 1, oy), (ox + nx * s + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy - 1), (ox, oy + ny * s + 3), "fixe", lw=0.8)
    for i in range(1, nx + 1): line(ax, [(ox + i * s, oy - 0.8), (ox + i * s, oy + 0.8)], "fixe", lw=0.6)
    for j in range(1, ny + 1): line(ax, [(ox - 0.8, oy + j * s), (ox + 0.8, oy + j * s)], "fixe", lw=0.6)
    text(ax, ox + nx * s + 5, oy - 2.5, "$" + xl + "$", "fixe", "s"); text(ax, ox - 3, oy + ny * s + 4, "$" + yl + "$", "fixe", "s")
    return lambda X, Y: (ox + X * s, oy + Y * s)

fig, ax = canvas(80)
P = axes(ax, 12, 8, 8, 3, 6)
line(ax, [P(0, 1), P(2.5, 6)], 'fixe', lw=1.2)
for X, dx, dy in ((0, 3, -3), (1, 3, -3), (2, 3, -3)):
    disc(ax, *P(X, 1 + 2 * X), 1.5, 'varie')
    text(ax, P(X, 1 + 2 * X)[0] + 3, P(X, 1 + 2 * X)[1] - 3.5, f'({X}, {1 + 2 * X})', 'varie', 's', ha='left')
box(ax, 52, 50, 34, 14, 'varie', label=r'$x,\ y$ : changent', size='s')
box(ax, 52, 28, 34, 14, 'fixe', label=r'$m,\ b$ : fixes', size='s')
text(ax, 69, 70, r'$y=mx+b$', 'encre', 'm')
text(ax, 69, 20, 'points de la droite', 'fixe', 's')
save(fig, '19-086')
