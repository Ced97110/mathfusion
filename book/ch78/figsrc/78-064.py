import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, nr, nc, cs, cells, size="s"):
    """Frame nr x nc; cells = {(row, col): (label, role)}, row 0 on top; absent cells are zeros."""
    box(ax, x, y, nc * cs, nr * cs, "fixe", fill=False, r=0.3, lw=0.6)
    for (r, c), (lab, role) in cells.items():
        box(ax, x + c * cs + 0.4, y + (nr - 1 - r) * cs + 0.4, cs - 0.8, cs - 0.8, role, label=lab, size=size, r=0.3)

fig, ax = canvas(60)
text(ax, 22, 54, r'$a\circ a=a^2$', 'resultat', 'm'); text(ax, 66, 54, r'$aa+aa$', 'limite', 'm')
cs = (11, 9)
def big(x, vals, role):
    for i, v in enumerate(vals):
        r, c = divmod(i, 2)
        box(ax, x + c * 11, 20 + (1 - r) * 10, 11, 10, role, label=v, size='m', r=0.4)
big(11, ['7', '10', '15', '22'], 'resultat'); big(55, ['14', '20', '30', '44'], 'limite')
text(ax, 44, 30, r'$\neq$', 'encre', 'xl')
text(ax, 22, 12, 'moyenne : ÷ 2', 'resultat', 's'); text(ax, 66, 12, 'sans ÷ 2 : le double', 'limite', 's')
text(ax, 44, 4, r'$a$ : 1, 2 / 3, 4', 'fixe', 's')
save(fig, '78-064')
