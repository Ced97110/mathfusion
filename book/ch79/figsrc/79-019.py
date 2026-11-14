import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, 'monter de 2 à 6, puis de 6 à 12', 'fixe', 's')
for c, n in [(12, '2'), (44, '6'), (76, '12')]:
    box(ax, c - 7, 12, 14, 9, 'sujet', label=n)
arrow(ax, (20, 16.5), (36, 16.5), 'varie'); arrow(ax, (52, 16.5), (68, 16.5), 'varie')
text(ax, 28, 13, '6 = 2 × 3', 'varie', 's'); text(ax, 60, 13, '12 = 6 × 2', 'varie', 's')
arrow(ax, (12, 22), (76, 22), 'resultat', curve=-0.3)
text(ax, 44, 36, '2 divise 12 : 12 = 2 × 6', 'resultat', 's')
text(ax, 44, 5, '12 = 2 × 3 × 2', 'resultat', 's')
save(fig, '79-019')
