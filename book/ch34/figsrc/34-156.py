import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, y0, u = 6, 12, 8
poly(ax, [(x0, y0), (x0 + 4 * u, y0), (x0, y0 + 3 * u)], 'fixe')
line(ax, [(x0 + 2, y0), (x0 + 2, y0 + 2), (x0, y0 + 2)], 'fixe', lw=0.6)
text(ax, x0 + 2 * u, y0 - 3.5, '4', 'fixe', 'm'); text(ax, x0 - 3, y0 + 1.5 * u, '3', 'fixe', 'm')
text(ax, x0 + 2 * u + 4, y0 + 1.5 * u + 3, '5', 'fixe', 'm')
text(ax, x0 + 4 * u - 6, y0 + 3, 'A', 'sujet', 'm'); text(ax, x0 + 3, y0 + 3 * u - 6, 'B', 'autre', 'm')
text(ax, 68, 52, 'tan A = 3/4', 'sujet', 'm'); text(ax, 68, 44, 'tan B = 4/3', 'autre', 'm')
text(ax, 68, 34, 'produit = 1', 'varie', 'm')
text(ax, 68, 24, 'A + B = 90°', 'resultat', 'm')
text(ax, 68, 14, 'tan 90°', 'encre', 'm'); text(ax, 68, 8, 'n’existe pas', 'encre', 'm')
save(fig, '34-156')
