import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# haut : 3 vecteurs du plan, un retiré
text(ax, 44, 79, 'famille de 3 vecteurs du plan', 'fixe', 's')
for i in range(3):
    disc(ax, 14 + i * 14, 68, 4.5, 'sujet' if i < 2 else 'varie')
arrow(ax, (49, 68), (59, 68), 'varie', lw=1.2)
text(ax, 54, 73, 'retirer 1', 'varie', 's')
for i in range(2):
    disc(ax, 66 + i * 14, 68, 4.5, 'resultat')
text(ax, 73, 58, '2 vecteurs : stop', 'resultat', 's')
text(ax, 73, 54, 'plus de retrait', 'resultat', 's')
line(ax, [(4, 47), (84, 47)], 'fixe', lw=0.6, dash=True)
# bas : V = {0}
text(ax, 44, 42, r'espace réduit à $\{0\}$', 'fixe', 's')
box(ax, 8, 24, 22, 10, 'varie', label='(0)')
text(ax, 19, 37, 'famille du vecteur nul', 'varie', 's')
arrow(ax, (32, 29), (52, 29), 'varie', lw=1.2)
text(ax, 42, 33, 'retirer', 'varie', 's')
box(ax, 54, 24, 30, 10, 'resultat', fill=False, dash=True, label='famille vide')
text(ax, 44, 15, 'c’est la base de {0}', 'resultat', 's')
text(ax, 44, 9, 'chaque retrait : −1 vecteur', 'fixe', 's')
text(ax, 44, 4, 'donc le tri s’arrête', 'fixe', 's')
save(fig, '58-286')
