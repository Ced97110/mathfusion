import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, nr, nc, cs, cells, size="s"):
    """Frame nr x nc; cells = {(row, col): (label, role)}, row 0 on top; absent cells are zeros."""
    box(ax, x, y, nc * cs, nr * cs, "fixe", fill=False, r=0.3, lw=0.6)
    for (r, c), (lab, role) in cells.items():
        box(ax, x + c * cs + 0.4, y + (nr - 1 - r) * cs + 0.4, cs - 0.8, cs - 0.8, role, label=lab, size=size, r=0.3)

fig, ax = canvas(52)
cs = 6.5
mats = [('X', 'sujet', {(0, 1): '1', (1, 0): '−1'}),
        ('Y', 'sujet', {(0, 2): '1', (2, 0): '−1'}),
        (r'$XY$', 'limite', {(1, 2): '−1'}),
        (r'$[X,Y]$', 'resultat', {(1, 2): '−1', (2, 1): '1'})]
for i, (name, role, vals) in enumerate(mats):
    x = 3 + 21.5 * i
    grid(ax, x, 18, 3, 3, cs, {k: (v, role) for k, v in vals.items()})
    text(ax, x + 9.75, 43, name if name.startswith('$') else f'${name}$', role, 'm')
text(ax, 55 - 0.5, 10, 'pas', 'limite', 's')
text(ax, 55 - 0.5, 6.5, 'antisymétrique', 'limite', 's')
text(ax, 76.5, 10, 'antisymétrique', 'resultat', 's')
text(ax, 22, 3, 'case vide = 0', 'fixe', 's')
save(fig, '78-056')
