import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
# le théorème : la liste complète
box(ax, 4, 75, 80, 12, 'resultat', label=r'liste complète : $\mathbb{Z}$ et $\mathbb{Z}/(d_i)$', size='s')
text(ax, 21, 70, 'ℤ : principal', 'resultat', 'm', weight='bold')
text(ax, 65, 70, 'ℤ[x] : pas principal', 'limite', 'm', weight='bold')
# gauche : un seul générateur
box(ax, 4, 41, 9, 9, 'sujet', label='2', weight='bold')
arrow(ax, (14, 45.5), (21, 45.5), 'varie')
box(ax, 22, 37, 18, 17, 'sujet', label='(2)')
text(ax, 21, 27, 'ℤ/(2) : 2 éléments', 'sujet', 's')
text(ax, 21, 14, 'dans la liste ℤ/(d)', 'resultat', 's')
# droite : deux générateurs
box(ax, 46, 49, 9, 9, 'autre', label='2', weight='bold')
box(ax, 46, 33, 9, 9, 'autre', label='x', weight='bold')
arrow(ax, (56, 53.5), (63, 47.5), 'varie')
arrow(ax, (56, 37.5), (63, 43.5), 'varie')
box(ax, 64, 37, 21, 17, 'autre', label='(2, x)')
text(ax, 65, 27, 'ℤ[x]/(2, x) : 2 éléments', 'autre', 's')
text(ax, 65, 21, 'aucun élément seul', 'limite', 's')
text(ax, 65, 14, 'pas dans la liste', 'limite', 's')
save(fig, '59-108')
