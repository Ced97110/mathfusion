import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, nr, nc, cs, cells, size="s"):
    """Frame nr x nc; cells = {(row, col): (label, role)}, row 0 on top; absent cells are zeros."""
    box(ax, x, y, nc * cs, nr * cs, "fixe", fill=False, r=0.3, lw=0.6)
    for (r, c), (lab, role) in cells.items():
        box(ax, x + c * cs + 0.4, y + (nr - 1 - r) * cs + 0.4, cs - 0.8, cs - 0.8, role, label=lab, size=size, r=0.3)

fig, ax = canvas(46)
text(ax, 30, 42, r'$X$ dans $Sk_3$', 'sujet', 'm')
cs = 9; x0, y0 = 6, 8
vals = {(0, 1): '1', (0, 2): '2', (1, 2): '3', (1, 0): '-1', (2, 0): '-2', (2, 1): '-3'}
cells = {}
for (r, c), v in vals.items():
    cells[(r, c)] = (v.replace('-', '−'), 'sujet' if c > r else 'autre')
for i in range(3): cells[(i, i)] = ('0', 'fixe')
grid(ax, x0, y0, 3, 3, cs, cells, 'm')
line(ax, [(x0, y0 + 27), (x0 + 27, y0)], 'varie', dash=True)
text(ax, 60, 34, r'${}^tX=-X$', 'sujet', 'l')
text(ax, 60, 27, 'chaque case est', 'encre', 's'); text(ax, 60, 23.5, 'l’opposée de sa case', 'encre', 's')
text(ax, 60, 20, 'en miroir', 'encre', 's')
text(ax, 60, 12, 'diagonale : 0', 'fixe', 's')
save(fig, '78-054')
