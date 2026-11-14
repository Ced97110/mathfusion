import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, ch, x, y = 11, 9, 33, 22
cells = {(0, 0): ('4', 'resultat', False), (0, 1): ('6', 'fixe', False),
         (1, 0): ('6', 'fixe', False), (1, 1): ('4', 'resultat', True)}
for (i, j), (v, role, dash) in cells.items():
    box(ax, x + j * cw, y + (1 - i) * ch, cw, ch, role, r=0.4, label=v, size='m', dash=dash, fill=not dash)
text(ax, 44, 52, 'valeurs absolues : 4, 6, 6, 4', 'fixe', 's')
text(ax, 15, y + ch + 4.5, 'pivot en (1, 1)', 'resultat', 's')
arrow(ax, (27, y + ch + 4.5), (x - 1, y + ch + 4.5), 'resultat', lw=1.0)
text(ax, 71, y + 4.5, 'aussi 4 en (2, 2)', 'resultat', 's')
arrow(ax, (59, y + 4.5), (x + 2 * cw + 1, y + 4.5), 'resultat', lw=1.0)
text(ax, 44, 10, 'le plus petit est déjà en place', 'resultat', 's')
save(fig, '59-110')
