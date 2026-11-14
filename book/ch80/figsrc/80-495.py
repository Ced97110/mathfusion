import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 63, 'chaîne 0, 1, 2', 'fixe', 'm')
for x, a, b in [(6, '0', '1'), (34, '1', '3'), (62, '2', '6')]:
    box(ax, x, 46, 20, 10, 'fixe', label=a)
    box(ax, x, 26, 20, 10, 'resultat', label=b)
    arrow(ax, (x + 10, 45), (x + 10, 37), 'varie')
arrow(ax, (27, 51), (33, 51), 'fixe'); arrow(ax, (55, 51), (61, 51), 'fixe')
text(ax, 30, 41, 'somme jusqu’ici', 'varie', 's')
text(ax, 4, 21, 'sommes partielles', 'resultat', 's', ha='left')
box(ax, 28, 4, 40, 11, 'sujet', label=r'$6 - 3 = 3$', size='l')
arrow(ax, (44, 25), (40, 16), 'varie'); arrow(ax, (72, 25), (58, 16), 'varie')
text(ax, 4, 9, 'valeur retrouvée', 'sujet', 's', ha='left')
save(fig, '80-495')
