import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, 'somme de la diagonale', 'encre', 'm')
x0, ytop, cw, ch = 8, 48, 14, 11
vals = [[1, 5], [7, 3]]
for r in range(2):
    for c in range(2):
        box(ax, x0 + c * cw, ytop - (r + 1) * ch, cw, ch, 'sujet' if r == c else 'fixe', label=str(vals[r][c]), size='m')
for sgn, xx in ((-1, x0 - 1.5), (1, x0 + 2 * cw + 1.5)):
    line(ax, [(xx - sgn * 1.5, ytop + 0.5), (xx, ytop + 0.5), (xx, ytop - 2 * ch - 0.5), (xx - sgn * 1.5, ytop - 2 * ch - 0.5)], 'encre', lw=0.9)
line(ax, [(x0 + cw / 2 + 2.5, ytop - ch / 2 - 2.2), (x0 + 1.5 * cw - 2.5, ytop - 1.5 * ch + 2.2)], 'sujet', lw=1.0, dash=True)
arrow(ax, (40, 37), (48, 37), 'resultat')
text(ax, 67, 37, 'trace = 1 + 3 = 4', 'resultat', 'm', weight='bold')
text(ax, 22, 20, '5 et 7 ne comptent pas', 'fixe', 's')
save(fig, '60-208')
