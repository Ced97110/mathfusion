import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 19, 61, r'$a<0$ : à gauche', 'sujet', 's'); text(ax, 69, 61, r'$|a|=-a$ : à droite', 'resultat', 's')
for y, a, b in [(42, '−3', '3'), (24, '−7', '7'), (6, '−100', '100')]:
    box(ax, 5, y, 28, 12, 'sujet', label=a, size='l')
    box(ax, 55, y, 28, 12, 'resultat', label=b, size='l')
    arrow(ax, (33, y + 6), (55, y + 6), 'varie')
text(ax, 44, 53, 'opposé', 'varie', 's')
save(fig, '13-046')
