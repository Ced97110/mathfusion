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

fig, ax = canvas(94)
text(ax, 6, 83, '$A$', 'sujet', 'l')
mat(ax, 20, 83, [[1, 2], [5, 6]], 'sujet', fills={(1, 0): 'sujet', (1, 1): 'sujet'})
cross(ax, 33, 83)
text(ax, 40, 83, '$B$', 'autre', 'l')
mat(ax, 54, 83, [[1, 0], [1, 1]], 'autre', fills={(0, 0): 'autre', (1, 0): 'autre'})
text(ax, 44, 72, 'ligne 2 de A, colonne 1 de B', 'sujet', 's')
text(ax, 30, 64, r'$AB$ : ligne 2, colonne 1', 'sujet', 's')
box(ax, 4, 47, 22, 10, 'sujet', label=r'$5\times1$'); text(ax, 30, 52, '+', 'sujet')
box(ax, 34, 47, 22, 10, 'sujet', label=r'$6\times1$'); box(ax, 60, 47, 24, 10, 'resultat', label=r'$=11$')
box(ax, 4, 19, 22, 10, 'autre', label=r'$1\times5$'); text(ax, 30, 24, '+', 'autre')
box(ax, 34, 19, 22, 10, 'autre', label=r'$1\times6$'); box(ax, 60, 19, 24, 10, 'resultat', label=r'$=11$')
arrow(ax, (15, 46.5), (15, 29.5), 'varie'); arrow(ax, (45, 46.5), (45, 29.5), 'varie')
text(ax, 30, 38, 'on échange', 'varie', 's')
text(ax, 80, 38, 'égales', 'resultat', 's')
arrow(ax, (72, 46.5), (72, 29.5), 'resultat', both=True)
text(ax, 30, 11, r'$B^TA^T$ : ligne 1, colonne 2', 'autre', 's')
save(fig, '52-214')
