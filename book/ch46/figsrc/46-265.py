import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 4, 34, 80, 22, 'fixe')
text(ax, 44, 61, 'G : les six mélanges de 3 cartes', 'fixe', 's')
for i in range(6):
    x = 12 + 13 * i
    if i == 0: disc(ax, x, 45, 4.2, 'resultat')
    else: disc(ax, x, 45, 4.2, 'fixe')
text(ax, 12, 37.5, 'neutre', 'resultat', 's')
box(ax, 4, 6, 36, 16, 'limite', fill=False, dash=True)
text(ax, 22, 14, 'H vide', 'limite', 'm')
text(ax, 62, 17, 'stable par produit :', 'resultat', 's')
text(ax, 62, 11, 'rien à multiplier', 'resultat', 's')
text(ax, 62, 3.5, 'mais pas de neutre', 'limite', 's')
arrow(ax, (12, 34), (18, 22.5), 'limite', lw=0.8)
save(fig, '46-265')
