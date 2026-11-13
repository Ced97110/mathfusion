import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
# la famille vide (0 vecteur) engendre {0} : combinaison vide = vecteur nul
box(ax, 4, 22, 28, 22, 'sujet', fill=False, dash=True)
text(ax, 18, 33, 'aucun\nvecteur', 'sujet', 's')
text(ax, 18, 48, 'famille vide', 'sujet', 'm', weight='bold')
arrow(ax, (33, 33), (51, 33), 'varie', lw=1.4)
text(ax, 42, 38, 'combinaison\nvide', 'varie', 's')
box(ax, 52, 20, 32, 26, 'resultat')
disc(ax, 68, 33, 3.2, 'resultat', label='0', size='l')
text(ax, 68, 50, r'espace $\{0\}$', 'resultat', 'm', weight='bold')
text(ax, 44, 10, r'0 vecteur dans la base : $\dim\{0\} = 0$', 'encre', 's')
save(fig, '58-190')
