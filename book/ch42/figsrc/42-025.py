import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r'$\{a,a,b\} = \{a,b\}$', 'sujet', 'xl')
for y, t, r in zip([40, 28, 16], ['gourde', 'carte', 'gourde'], ['varie', 'fixe', 'varie']):
    box(ax, 4, y - 4.5, 22, 9, r, label=t, size='s')
text(ax, 15, 7, '3 lignes écrites', 'fixe', 's')
arrow(ax, (28, 28), (44, 28), 'varie')
box(ax, 46, 12, 38, 32, 'resultat')
box(ax, 55, 30, 20, 9, 'varie', label='gourde', size='s'); box(ax, 55, 17, 20, 9, 'fixe', label='carte', size='s')
text(ax, 65, 7, '2 objets dans le sac', 'resultat', 's')
save(fig, '42-025')
