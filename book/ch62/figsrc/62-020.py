import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 34, 84, 'départ', 'fixe', 's')
box(ax, 8, 68, 52, 11, 'sujet', label='$(j\\,r_1)^3$')
arrow(ax, (34, 67.5), (34, 59.5), 'varie')
text(ax, 37, 63.5, 'cube d’un produit', 'varie', 's', ha='left')
box(ax, 8, 48, 52, 11, 'sujet', label='$= j^3\\,r_1^3$')
arrow(ax, (34, 47.5), (34, 39.5), 'varie')
text(ax, 37, 43.5, 'on remplace', 'varie', 's', ha='left')
box(ax, 8, 28, 52, 11, 'varie', lw=2.0, label='$= 1 \\times 2$')
text(ax, 63, 33.5, 'étape\nqui conclut', 'varie', 's', ha='left')
arrow(ax, (34, 27.5), (34, 19.5), 'varie')
box(ax, 8, 8, 52, 11, 'resultat', label='$= 2$')
text(ax, 2, 56, '$j^3 = 1$', 'encre', 's', ha='left') if False else None
text(ax, 2, 14, 'arrivée', 'fixe', 's', ha='left') if False else None
text(ax, 44, 3, '$j^3 = 1$ et $r_1^3 = 2$', 'encre', 's')
save(fig, '62-020')
