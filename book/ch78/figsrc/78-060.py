import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, nr, nc, cs, cells, size="s"):
    """Frame nr x nc; cells = {(row, col): (label, role)}, row 0 on top; absent cells are zeros."""
    box(ax, x, y, nc * cs, nr * cs, "fixe", fill=False, r=0.3, lw=0.6)
    for (r, c), (lab, role) in cells.items():
        box(ax, x + c * cs + 0.4, y + (nr - 1 - r) * cs + 0.4, cs - 0.8, cs - 0.8, role, label=lab, size=size, r=0.3)

fig, ax = canvas(58)
text(ax, 20, 52, r'$\mathbb{R}^3$ avec $\times$', 'sujet', 'm')
text(ax, 67, 52, r'$Sk_3$ avec crochet', 'autre', 'm')
box(ax, 4, 22, 32, 12, 'sujet', label=r'$(1,\,2,\,3)$', size='l')
cs = 8
M = [['0', '−3', '2'], ['3', '0', '−1'], ['−2', '1', '0']]
cells = {(r, c): (M[r][c], 'fixe' if r == c else 'autre') for r in range(3) for c in range(3)}
grid(ax, 55, 17, 3, 3, cs, cells, 'm')
arrow(ax, (37, 28), (53, 28), 'resultat', both=True)
text(ax, 45, 33, 'même', 'resultat', 's'); text(ax, 45, 23.5, 'algèbre', 'resultat', 's')
text(ax, 44, 8, 'un calcul se refait dans l’autre', 'encre', 's')
save(fig, '78-060')
