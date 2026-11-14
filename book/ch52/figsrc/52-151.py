import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, y0, d = 16, 14, 8.5
for a in range(6):
    for b in range(6):
        disc(ax, x0 + a * d, y0 + b * d, 1.3, 'resultat' if a == b else 'fixe')
disc(ax, x0 + 1 * d, y0 + 2 * d, 1.6, 'limite', fill=False)
text(ax, x0 + 1 * d - 7, y0 + 2 * d + 4, '(1, 2)', 'limite', 's')
text(ax, x0 + 2 * d + 9, y0 + 2 * d - 4, '(2, 2)', 'resultat', 's')
text(ax, x0 + 5 * d, y0 + 5 * d + 6, '(5, 5)', 'resultat', 's', ha='center')
text(ax, 44, 5, "im $\\eta$ : 6 paires sur 36 dans $R'$", 'resultat', 's')
text(ax, 62, 30, 'non atteinte', 'limite', 's') if False else None
text(ax, 70, 38, 'atteintes', 'resultat', 's')
save(fig, '52-151')
