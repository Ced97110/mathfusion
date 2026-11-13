import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
k = 0.4
fig, ax = canvas(64)
text(ax, 44, 60, 'quatre longueurs sous la racine', 'fixe', 'm')
box(ax, 8, 34, 75*k, 35*k, 'sujet', label='2 625 m²', r=0.5)
text(ax, 8 + 75*k/2, 30.5, '75', 'sujet', 'm'); text(ax, 5, 34 + 35*k/2, '35', 'sujet', 'm')
box(ax, 54, 34, 25*k, 15*k, 'autre', r=0.4)
text(ax, 54 + 25*k/2, 30.5, '25', 'autre', 'm'); text(ax, 54 + 25*k + 3, 34 + 15*k/2, '15', 'autre', 'm')
text(ax, 54 + 25*k/2, 34 + 15*k + 3.5, '375 m²', 'autre', 'm')
text(ax, 45, 41, '×', 'encre', 'l')
text(ax, 44, 21, '2 625 × 375 = 984 375 m⁴', 'varie', 'm')
arrow(ax, (44, 18), (44, 11), 'varie')
text(ax, 44, 6, '√ = 992,2 m²', 'resultat', 'l', weight='bold')
save(fig, '37-089')
