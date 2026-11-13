import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 20, 38, 48, 10, 'resultat', label='dette de 2 €')
box(ax, 6, 14, 12, 10, 'limite', fill=False, dash=True, label='?')
for i, s in enumerate(['0', '1', '2', '3', '…']):
    box(ax, 22 + i * 12.5, 14, 11, 10, 'fixe', label=s)
arrow(ax, (38, 38), (13, 25.5), 'limite')
text(ax, 62, 31, 'le résultat existe', 'resultat', 's')
text(ax, 44, 7, 'aucun nombre pour l’écrire', 'limite', 'm')
save(fig, '13-004')
