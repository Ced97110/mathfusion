import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 59, 'coefficients', 'varie', 'm', weight='bold')
for r in range(3):
    for c in range(3):
        x, y = 8 + 9 * c, 24 + 9 * r
        box(ax, x, y, 9, 9, 'varie', r=0.4)
        for d in (-2.6, 0, 2.6): disc(ax, x + 4.5 + d, y + 4.5, 0.9, 'varie')
text(ax, 21.5, 19, 'chaque case : 3 produits', 'varie', 's')
text(ax, 21.5, 13, '6 termes de 3 cases', 'varie', 's')
text(ax, 70, 59, 'niveau du haut', 'resultat', 'm', weight='bold')
box(ax, 54, 30, 32, 22, 'resultat')
text(ax, 70, 44, 'composer', 'resultat', 's'); text(ax, 70, 37, r'$=\det A\times\det B$', 'resultat', 's')
text(ax, 70, 22, 'une phrase', 'resultat', 's')
line(ax, [(51, 8), (51, 54)], 'fixe', dash=True)
save(fig, '76-111')
