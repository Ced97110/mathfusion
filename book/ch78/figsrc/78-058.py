import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, nr, nc, cs, cells, size="s"):
    """Frame nr x nc; cells = {(row, col): (label, role)}, row 0 on top; absent cells are zeros."""
    box(ax, x, y, nc * cs, nr * cs, "fixe", fill=False, r=0.3, lw=0.6)
    for (r, c), (lab, role) in cells.items():
        box(ax, x + c * cs + 0.4, y + (nr - 1 - r) * cs + 0.4, cs - 0.8, cs - 0.8, role, label=lab, size=size, r=0.3)

fig, ax = canvas(54)
text(ax, 44, 50, 'rotation d’un angle de 0,01', 'varie', 'm')
cs = 14
L = {(0, 0): ('−0,00005', 'fixe'), (0, 1): ('−0,01', 'sujet'), (1, 0): ('0,01', 'sujet'), (1, 1): ('−0,00005', 'fixe')}
R = {(0, 0): ('0', 'fixe'), (0, 1): ('−0,01', 'sujet'), (1, 0): ('0,01', 'sujet'), (1, 1): ('0', 'fixe')}
grid(ax, 3, 8, 2, 2, cs, L); grid(ax, 57, 8, 2, 2, cs, R)
text(ax, 17, 42, 'écart à l’identité', 'encre', 's')
text(ax, 71, 42, 'matrice antisymétrique', 'sujet', 's')
text(ax, 44, 22, r'$\approx$', 'varie', 'xl')
text(ax, 44, 3, 'diagonale presque nulle', 'fixe', 's')
save(fig, '78-058')
