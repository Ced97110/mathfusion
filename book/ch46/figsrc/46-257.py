import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
xs = [14 + 20 * i for i in range(4)]
top = ['0', '1', '2', '3']; bot = ['0', '¼', '½', '¾']
D = 22
for i, x in enumerate(xs):
    sub = i in (0, 2)
    disc(ax, x, 46 + D, 4.5, 'varie' if sub else 'sujet', label=top[i])
    disc(ax, x, 15 + D, 4.5, 'varie' if sub else 'autre', label=bot[i])
    arrow(ax, (x, 46 + D - 5), (x, 15 + D + 5), 'varie' if sub else 'fixe', lw=1.0 if sub else 0.7)
text(ax, 44, 57 + D, 'horloge à 4 heures', 'sujet', 'm')
text(ax, 44, 4.5 + D, 'rotations du carré (en tours)', 'autre', 'm')
text(ax, 44, 16, 'sous-groupes du haut : {0}, {0, 2}, tout', 'sujet', 's')
text(ax, 44, 10, 'images : {0}, {0, ½}, tout', 'autre', 's')
text(ax, 44, 4, 'même nombre : 3 et 3', 'resultat', 's')
save(fig, '46-257')
