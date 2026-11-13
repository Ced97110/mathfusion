import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, rows, role='sujet', c=6.5, fills=None, size='m'):
    n = len(rows); m = len(rows[0]); x0 = cx - m * c / 2; y0 = cy - n * c / 2
    for (i, j), r in (fills or {}).items():
        box(ax, x0 + j * c + 0.4, y0 + (n - 1 - i) * c + 0.4, c - 0.8, c - 0.8, r, r=0.3, lw=0.4)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            if v != '': text(ax, x0 + (j + .5) * c, y0 + (n - 1 - i + .5) * c, str(v), role, size)
    for sx, d in ((x0 - 0.8, 1), (x0 + m * c + 0.8, -1)):
        line(ax, [(sx + d * 1.4, y0 - 0.5), (sx, y0 - 0.5), (sx, y0 + n * c + 0.5), (sx + d * 1.4, y0 + n * c + 0.5)], role, lw=1.0)

def cross(ax, x, y, role='encre'):
    line(ax, [(x - 1.5, y - 1.5), (x + 1.5, y + 1.5)], role); line(ax, [(x - 1.5, y + 1.5), (x + 1.5, y - 1.5)], role)

def eq(ax, x, y, role='encre'):
    line(ax, [(x - 1.6, y + 0.9), (x + 1.6, y + 0.9)], role); line(ax, [(x - 1.6, y - 0.9), (x + 1.6, y - 0.9)], role)

fig, ax = canvas(90)
text(ax, 44, 84, 'transposer chaque matrice', 'varie', 'm')
box(ax, 2, 64, 40, 12, 'sujet', label=r'$A^T$ : (1, 5) (2, 6)', size='s')
box(ax, 46, 64, 40, 12, 'autre', label=r'$B^T$ : (1, 1) (0, 1)', size='s')
arrow(ax, (22, 64), (22, 50.5), 'varie'); arrow(ax, (66, 64), (66, 50.5), 'varie')
text(ax, 44, 57, "multiplier à l'envers", 'varie', 's')
box(ax, 2, 38, 84, 12, 'resultat', label=r'$B^TA^T$ : (3, 11) (2, 6)', size='m')
text(ax, 44, 31, '=', 'resultat', 'l')
box(ax, 2, 12, 84, 12, 'sujet', label=r'$(AB)^T$ : (3, 11) (2, 6)', size='m')
text(ax, 44, 6, r'transposée du produit $AB$', 'sujet', 's')
save(fig, '52-215')
