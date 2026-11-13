import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 78, 'chaque entier est dans un seul groupe', 'sujet', 'm')
groups = ['0', '3 et −3', '5 et −5', '12 et −12']
for i, g in enumerate(groups):
    box(ax, 2 + i * 21.5, 52, 19.5, 14, 'sujet', label=g, size='s')
text(ax, 44, 45, 'a ∼ b : chaque nombre divise l’autre', 'sujet', 's')
# contre-exemple : une seule moitié
text(ax, 44, 34, 'avec seulement a ∣ b', 'encre', 'm')
box(ax, 6, 8, 18, 14, 'fixe', label='a = 3')
box(ax, 64, 8, 18, 14, 'fixe', label='b = 12')
arrow(ax, (24.8, 17), (63.2, 17), 'resultat')
text(ax, 44, 21.5, '3 ∣ 12 : vrai', 'resultat', 's')
arrow(ax, (63.2, 11), (24.8, 11), 'limite')
text(ax, 44, 6.5, '12 ∣ 3 : faux', 'limite', 's')
save(fig, '56-040')
