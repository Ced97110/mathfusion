import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def node(x, y, s, role='sujet'):
    box(ax, x - 6, y - 4, 12, 8, role, label=s)
# réflexive
text(ax, 4, 74, 'réflexive', 'encre', 'm', ha='left')
node(42, 74, '$A$'); node(72, 74, '$A$')
arrow(ax, (48.8, 74), (65.2, 74), 'varie'); text(ax, 57, 78.5, r'$P=Q=1$', 'varie', 's')
# symétrique
text(ax, 4, 48, 'symétrique', 'encre', 'm', ha='left')
node(42, 48, '$A$'); node(72, 48, '$B$', 'autre')
arrow(ax, (48.8, 50), (65.2, 50), 'varie'); text(ax, 57, 54, r'$P,\,Q$', 'varie', 's')
arrow(ax, (65.2, 46), (48.8, 46), 'resultat'); text(ax, 57, 41.5, r'$P^{-1},\,Q^{-1}$', 'resultat', 's')
# transitive
text(ax, 4, 22, 'transitive', 'encre', 'm', ha='left')
node(36, 22, '$A$'); node(58, 22, '$B$', 'autre'); node(80, 22, '$C$')
arrow(ax, (42.8, 22), (51.2, 22), 'varie'); arrow(ax, (64.8, 22), (73.2, 22), 'varie')
arrow(ax, (36, 17.4), (80, 17.4), 'resultat', curve=0.35)
text(ax, 58, 4.5, 'produits des matrices', 'resultat', 's')
save(fig, '59-050')
