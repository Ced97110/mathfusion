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

fig, ax = canvas(98)
box(ax, 6, 82, 76, 12, 'sujet', label=r'départ : $A$ 2×3, $B$ 3×1', size='m')
arrow(ax, (44, 82), (44, 74.5), 'fixe')
box(ax, 14, 60, 60, 14, 'varie', label=r'$(AB)^T$ doit être $1\times2$', size='m', lw=1.8)
arrow(ax, (30, 60), (22, 48.5), 'fixe'); arrow(ax, (58, 60), (66, 48.5), 'fixe')
box(ax, 2, 34, 40, 14, 'resultat', label=r'$B^TA^T$ : 1×3 puis 3×2', size='s')
box(ax, 46, 34, 40, 14, 'limite', label=r'$A^TB^T$ : 3×2 puis 1×3', size='s')
text(ax, 22, 29, 'existe : 1×2', 'resultat', 's'); text(ax, 66, 29, 'impossible', 'limite', 's')
arrow(ax, (22, 26), (30, 20.5), 'resultat')
box(ax, 6, 6, 76, 14, 'resultat', label=r'$B^TA^T$ = (6  15) = $(AB)^T$', size='m')
save(fig, '52-213')
