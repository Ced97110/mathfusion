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

def rect(ax, x, cy, w, h, role, name, dims):
    box(ax, x, cy - h / 2, w, h, role, label=name, size='s', r=0.4)
    text(ax, x + w / 2, cy - h / 2 - 3, dims, role, 's')
fig, ax = canvas(98)
rect(ax, 6, 86, 18, 12, 'sujet', r'$A$', r'$2\times3$'); cross(ax, 29, 86)
rect(ax, 34, 86, 6, 18, 'autre', r'$B$', r'$3\times1$'); eq(ax, 45, 86)
rect(ax, 50, 86, 6, 12, 'resultat', r'$AB$', r'$2\times1$')
rect(ax, 6, 52, 18, 6, 'autre', r'$B^T$', r'$1\times3$'); cross(ax, 29, 52)
rect(ax, 34, 52, 12, 18, 'sujet', r'$A^T$', r'$3\times2$'); eq(ax, 51, 52)
rect(ax, 56, 52, 12, 6, 'resultat', r'$B^TA^T$', r'$1\times2$')
text(ax, 79, 52, r'$3=3$', 'resultat', 's')
rect(ax, 6, 18, 12, 18, 'sujet', r'$A^T$', r'$3\times2$'); cross(ax, 23, 18)
rect(ax, 28, 18, 18, 6, 'autre', r'$B^T$', r'$1\times3$')
line(ax, [(5, 11), (47, 25)], 'limite', lw=1.2)
text(ax, 68, 18, r'$2\neq1$ : impossible', 'limite', 's')
save(fig, '52-212')
