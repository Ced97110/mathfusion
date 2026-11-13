import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = lambda v: 44 + v * 3.6
disc(ax, 28, 50, 4.5, 'sujet', label='3')
disc(ax, 60, 50, 4.5, 'autre', label='−3')
box(ax, 6, 22, 76, 12, 'resultat', fill=False, dash=True)
for v in range(-9, 10, 3):
    disc(ax, f(v), 28, 1.0, 'resultat')
arrow(ax, (28, 45), (28, 35), 'varie')
arrow(ax, (60, 45), (60, 35), 'varie')
text(ax, 44, 50, 'lequel ?', 'varie', 's')
text(ax, 44, 15, '(3) = (−3)', 'resultat', 'm')
text(ax, 44, 7, "l'ensemble ne garde pas le signe", 'fixe', 's')
save(fig, '56-096')
