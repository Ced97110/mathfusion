import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(66)
c = 7.0; g = 1
def bloc(x0, y0, nl, nc, rx, ry, ty):
    for i in range(nl):
        box(ax, x0, y0 + (nl - 1 - i) * c, c - 0.6, c - 0.6, 'sujet', r=0.3)
    for j in range(nc):
        box(ax, x0 + 9 + j * c, y0 + nl * c + 1, c - 0.6, c - 0.6, 'autre', r=0.3)
    for i in range(nl):
        for j in range(nc):
            box(ax, x0 + 9 + j * c, y0 + (nl - 1 - i) * c, c - 0.6, c - 0.6, 'fixe', r=0.3)
bloc(5, 18, 2, 2, 0, 0, 0)
bloc(49, 18, 2, 3, 0, 0, 0)
text(ax, 25, 60, 'matrice carrée', 'resultat', 's'); text(ax, 68, 60, 'matrice non carrée', 'limite', 's')
text(ax, 25, 50, r'$x$ : 2 coordonnées', 'sujet', 's'); text(ax, 25, 45, r'$y$ : 2 coordonnées', 'autre', 's')
text(ax, 68, 50, r'$x$ : 2 coordonnées', 'sujet', 's'); text(ax, 68, 45, r'$y$ : 3 coordonnées', 'autre', 's')
text(ax, 25, 9, r'$x = y$ possible', 'resultat', 's'); text(ax, 68, 9, r'$x = y$ impossible', 'limite', 's')
save(fig, '71-059')
