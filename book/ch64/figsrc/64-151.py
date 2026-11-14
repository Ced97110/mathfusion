import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# départ : un renommage est connu par son exposant k
box(ax, 14, 66, 60, 12, 'sujet', label=r'$\eta(z)=z^k$ : connu par $k$')
arrow(ax, (30, 65.5), (22, 55.5), 'fixe')
arrow(ax, (58, 65.5), (66, 55.5), 'fixe')
text(ax, 44, 61, 'deux renommages', 'fixe', 's')

# étape qui porte le poids : deux ordres, exposants multipliés
box(ax, 2, 40, 40, 15, 'varie', label=r'$k=2$, puis $l=3$' + '\n' + r'$2\times 3=6$')
box(ax, 46, 40, 40, 15, 'autre', label=r'$l=3$, puis $k=2$' + '\n' + r'$3\times 2=6$')
arrow(ax, (22, 39.5), (35, 29.5), 'fixe')
arrow(ax, (66, 39.5), (53, 29.5), 'fixe')

# arrivée : même exposant, donc commutation
box(ax, 14, 14, 60, 15, 'resultat', label=r'$z^6=z$ car $z^5=1$' + '\n' + 'même résultat')
text(ax, 44, 6, 'le produit des entiers ne dépend pas de l\'ordre', 'resultat', 's')
save(fig, '64-151')
