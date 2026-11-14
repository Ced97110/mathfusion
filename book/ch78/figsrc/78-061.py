import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, nr, nc, cs, cells, size="s"):
    """Frame nr x nc; cells = {(row, col): (label, role)}, row 0 on top; absent cells are zeros."""
    box(ax, x, y, nc * cs, nr * cs, "fixe", fill=False, r=0.3, lw=0.6)
    for (r, c), (lab, role) in cells.items():
        box(ax, x + c * cs + 0.4, y + (nr - 1 - r) * cs + 0.4, cs - 0.8, cs - 0.8, role, label=lab, size=size, r=0.3)

fig, ax = canvas(66)
cs = 8; half = r'$\frac{1}{2}$'
grid(ax, 4, 38, 2, 2, cs, {(0, 0): ('1', 'sujet')}); text(ax, 12, 59, r'$ab$', 'sujet', 'm')
grid(ax, 30, 38, 2, 2, cs, {(1, 1): ('1', 'autre')}); text(ax, 38, 59, r'$ba$', 'autre', 'm')
grid(ax, 62, 38, 2, 2, cs, {(0, 0): ('1', 'fixe'), (1, 1): ('1', 'fixe')}); text(ax, 70, 59, r'$ab+ba$', 'fixe', 'm')
text(ax, 23, 46, '+', 'encre', 'xl'); text(ax, 51, 46, '=', 'encre', 'xl')
arrow(ax, (70, 36), (70, 27.5), 'varie'); text(ax, 78, 31.5, r'$\div 2$', 'varie', 'm')
grid(ax, 62, 10, 2, 2, cs, {(0, 0): (half, 'resultat'), (1, 1): (half, 'resultat')}); text(ax, 70, 5, r'$a\circ b$', 'resultat', 'm')
text(ax, 28, 14, 'case vide = 0', 'fixe', 's')
save(fig, '78-061')
