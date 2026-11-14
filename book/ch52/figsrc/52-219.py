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

fig, ax = canvas(60)
def g(cx, pos, lab, name, where):
    fl = {(i, j): 'fixe' for i in range(2) for j in range(2)}; fl[pos] = 'varie'
    rows = [['', ''], ['', '']]; rows[pos[0]][pos[1]] = 2
    mat(ax, cx, 34, rows, 'sujet', fills=fl)
    text(ax, cx, 18, lab, 'sujet', 'm'); text(ax, cx, 11, where, 'fixe', 's')
g(14, (0, 1), r'$A$', '', 'ligne 1, col. 2')
g(44, (1, 0), r'$A^T$', '', 'ligne 2, col. 1')
g(74, (0, 1), r'$(A^T)^T$', '', 'ligne 1, col. 2')
arrow(ax, (25, 34), (33, 34), 'varie'); text(ax, 29, 40, 'échanger', 'varie', 's')
arrow(ax, (55, 34), (63, 34), 'varie'); text(ax, 59, 40, 'échanger', 'varie', 's')
text(ax, 44, 53, 'le 2 revient à sa place', 'resultat', 'm')
save(fig, '52-219')
