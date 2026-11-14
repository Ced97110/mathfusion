import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(56)
c = 5; ytop = 44
for x, n in ((6, 4), (50, 5)):
    for i in range(n):
        for j in range(n):
            inb = i < 4 and j < 4 and i // 2 == j // 2
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, 'sujet' if inb else 'fixe', r=0.3, lw=0.6)
    for b in range(2):
        text(ax, x + b * 2 * c + c, ytop - b * 2 * c - c, r'$S$', 'sujet', 'm')
text(ax, 16, 48, '4 × 4', 'sujet', 'm'); text(ax, 62.5, 48, '5 × 5', 'sujet', 'm')
text(ax, 16, 14, r'rang $4=2\times 2$', 'resultat', 's'); text(ax, 16, 9, 'déterminant 1', 'resultat', 's')
text(ax, 62.5, 14, 'rang 4', 'resultat', 's'); text(ax, 62.5, 9, 'déterminant 0', 'resultat', 's')
text(ax, 81, 21.5, 'zéros', 'fixe', 's')
save(fig, '71-105')
