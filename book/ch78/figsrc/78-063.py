import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, nr, nc, cs, cells, size="s"):
    """Frame nr x nc; cells = {(row, col): (label, role)}, row 0 on top; absent cells are zeros."""
    box(ax, x, y, nc * cs, nr * cs, "fixe", fill=False, r=0.3, lw=0.6)
    for (r, c), (lab, role) in cells.items():
        box(ax, x + c * cs + 0.4, y + (nr - 1 - r) * cs + 0.4, cs - 0.8, cs - 0.8, role, label=lab, size=size, r=0.3)

fig, ax = canvas(58)
half = r'$\frac{1}{2}$'
for y, head, first, second, r1, r2 in [(34, r'$a\circ b$', 'ab', 'ba', 'sujet', 'autre'), (10, r'$b\circ a$', 'ba', 'ab', 'autre', 'sujet')]:
    text(ax, 8, y + 6, head, 'encre', 'm')
    box(ax, 17, y, 14, 12, r1, label=f'${first}$')
    text(ax, 35, y + 6, '+', 'encre', 'l')
    box(ax, 39, y, 14, 12, r2, label=f'${second}$')
    arrow(ax, (54, y + 6), (60, 28), 'varie')
grid(ax, 62, 20, 2, 2, 8, {(0, 0): (half, 'resultat'), (1, 1): (half, 'resultat')})
text(ax, 70, 47, r'$\div 2$', 'varie', 'm')
text(ax, 70, 14, 'même matrice', 'resultat', 's')
text(ax, 44, 3, 'somme : l’ordre ne compte pas', 'fixe', 's')
text(ax, 70, 8, 'case vide = 0', 'fixe', 's')
save(fig, '78-063')
