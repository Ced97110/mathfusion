import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, s, nx, ny, xl="x", yl="y"):
    arrow(ax, (ox - 1, oy), (ox + nx * s + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy - 1), (ox, oy + ny * s + 3), "fixe", lw=0.8)
    for i in range(1, nx + 1): line(ax, [(ox + i * s, oy - 0.8), (ox + i * s, oy + 0.8)], "fixe", lw=0.6)
    for j in range(1, ny + 1): line(ax, [(ox - 0.8, oy + j * s), (ox + 0.8, oy + j * s)], "fixe", lw=0.6)
    text(ax, ox + nx * s + 5, oy - 2.5, "$" + xl + "$", "fixe", "s"); text(ax, ox - 3, oy + ny * s + 4, "$" + yl + "$", "fixe", "s")
    return lambda X, Y: (ox + X * s, oy + Y * s)

fig, ax = canvas(75)
P = axes(ax, 10, 8, 8, 3, 6)
line(ax, [P(-0.0, 1), P(2.5, 6)], 'fixe', lw=1.2)
disc(ax, *P(0, 1), 1.6, 'sujet')
text(ax, P(0, 1)[0] + 3, P(0, 1)[1] - 3.5, r'$(0,\ b)$', 'sujet', 's', ha='left')
text(ax, 10, 70, r'$y=mx+b$', 'encre', 'l', ha='left')
box(ax, 50, 40, 36, 14, 'varie', label=r'$y$ quand $x=0$', size='m')
arrow(ax, (68, 39), (68, 29), 'varie')
box(ax, 50, 12, 36, 16, 'sujet', label=r'$b=1$', size='l')
text(ax, 68, 63, 'à répéter à chaque fois', 'fixe', 's')
arrow(ax, (50, 14), (P(0, 1)[0] + 3, P(0, 1)[1] + 1.5), 'sujet', curve=-0.0)
save(fig, '19-085')
