import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
s = 26.0; x0, y0 = 8, 14
A, B, C, D = (x0, y0), (x0+s, y0), (x0+s, y0+s), (x0, y0+s)
poly(ax, [A, B, C, D], 'fixe')
line(ax, [A, B], 'sujet', lw=2.4); line(ax, [A, C], 'varie', lw=2.4)
for p, n, dx, dy in ((A, 'A', -3.5, -3.5), (B, 'B', 3.5, -3.5), (C, 'C', 3.5, 3.5), (D, 'D', -3.5, 3.5)):
    text(ax, p[0]+dx, p[1]+dy, n, 'encre', 'm')
bx = 46
ax.plot([bx, bx + s], [40, 40], color=COL['sujet'], lw=2.4, solid_capstyle='butt')
text(ax, bx, 44, 'côté AB : 1', 'sujet', 's', ha='left')
ax.plot([bx, bx + s*2**0.5], [24, 24], color=COL['varie'], lw=2.4, solid_capstyle='butt')
text(ax, bx, 28, 'diagonale AC : √2', 'varie', 's', ha='left')
text(ax, 62, 52, 'coins voisins', 'sujet', 's'); text(ax, 62, 10, 'coins non voisins', 'varie', 's')
save(fig, '22-015')
