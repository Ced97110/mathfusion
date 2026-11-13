import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
s = 8
x0, y0 = 8, 14
P = [(x0, y0), (x0 + 4 * s, y0), (x0 + 4 * s, y0 + 3 * s), (x0, y0 + 3 * s)]
poly(ax, [P[0], P[1], P[2]], 'sujet')
poly(ax, [P[0], P[2], P[3]], 'autre')
line(ax, [P[0], P[2]], 'encre', lw=1.0)
cx, cy = x0 + 2 * s, y0 + 1.5 * s
disc(ax, cx, cy, 0.9, 'varie')
arrow(ax, (x0 + 3 * s, y0 + 0.5 * s), (x0 + 1 * s, y0 + 2.5 * s), 'varie', curve=-0.5)
text(ax, x0 + 2 * s, y0 - 4, '4 cm', 'fixe', 's')
text(ax, x0 - 4, y0 + 1.5 * s, '3 cm', 'fixe', 's', rot=90)
text(ax, 66, 46, 'demi-tour', 'varie', 'm', weight='bold')
text(ax, 66, 41, 'autour du centre', 'varie', 's')
text(ax, 66, 31, 'triangle bleu : 6', 'sujet', 's')
text(ax, 66, 25, 'triangle violet : 6', 'autre', 's')
text(ax, 66, 15, 'même aire : 12 ÷ 2', 'resultat', 's')
save(fig, '11-110')
