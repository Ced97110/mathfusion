import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, 'Groupe de 12 éléments', 'encre', 'm')
box(ax, 3, 20, 31, 24, 'sujet')
text(ax, 18.5, 39, 'décrit par sa taille', 'sujet', 's')
for i in range(4):
    disc(ax, 8 + 6.5 * i, 28, 2.3, 'sujet')
text(ax, 18.5, 13, r'4 éléments $=2^2$', 'sujet', 'm')
arrow(ax, (36, 32), (54, 32), 'varie')
text(ax, 45, 37, 'existe ?', 'varie', 'm')
box(ax, 56, 20, 29, 24, 'fixe', fill=False, dash=True)
text(ax, 70.5, 32, '?', 'fixe', 'xl')
text(ax, 70.5, 13, 'pas encore prouvé', 'limite', 's')
save(fig, '50-039')
