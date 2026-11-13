import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cw = 80 / 12
cx = lambda k: 4 + (k + 0.5) * cw
for k in range(12):
    box(ax, 4 + k * cw, 8, cw, 8, 'resultat', lw=0.7, r=0.5)
text(ax, cx(2), 12, '2', 'resultat', 's'); text(ax, cx(5), 12, '5', 'resultat', 's')
text(ax, 44, 3.5, r'$M$ : les 12 heures, toutes atteintes', 'resultat', 's')
for v, x in (('14', 7.5), ('2', cx(2)), ('5', cx(5))):
    box(ax, x - 5, 36, 10, 8, 'sujet', label=v)
text(ax, 22, 49, 'entiers', 'sujet', 's')
arrow(ax, (7.5, 35.6), (cx(2) - 1.4, 16.5), 'varie')
arrow(ax, (cx(2), 35.6), (cx(2) + 0.6, 16.5), 'varie')
arrow(ax, (cx(5), 35.6), (cx(5), 16.5), 'varie')
text(ax, 66, 42, r'$\eta$ : entier $\mapsto$ heure', 'encre', 'm')
text(ax, 66, 31, '2 et 14 : même heure', 'varie', 's')
save(fig, '59-035')
