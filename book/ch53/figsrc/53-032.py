import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 2, 28, 26, 11, 'varie', label='DOJHEUH', weight='bold')
text(ax, 15, 43, 'message intercepté', 'varie', 's')
# Hugo : avec la clé
arrow(ax, (28, 36), (54, 52), 'resultat')
text(ax, 62, 64, 'Hugo, avec la clé 3', 'resultat', 's')
box(ax, 54, 47, 32, 11, 'resultat', label='ALGEBRE')
# espion : sans la clé
arrow(ax, (28, 31), (54, 15), 'autre')
box(ax, 54, 9, 32, 11, 'autre', fill=True, dash=True, label='ALGEBRE ?')
text(ax, 62, 3.5, 'l’espion, sans la clé', 'autre', 's')
save(fig, '53-032')
