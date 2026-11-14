import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$|G|=|Z(G)|+0$', 'resultat', 'l')
w = 6.4; x = 5.6
for i in range(12): box(ax, x + i * w, 38, w, 9, 'fixe', r=0.6)
brace(ax, x, x + 12 * w, 38, 'fixe', label=r'$Z(G)=G$ : 12 éléments')
text(ax, 44, 52, 'chaque élément est seul', 'fixe', 's')
box(ax, 14, 8, 60, 10, 'varie', fill=False, dash=True, label='classe de plus de 1 : aucune')
text(ax, 44, 22, 'somme vide', 'varie', 's')
save(fig, '50-144')
