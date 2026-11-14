import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 4, 12, 26, 52, 'sujet')
box(ax, 44, 12, 40, 52, 'autre')
text(ax, 17, 59, 'entiers', 'sujet', 's')
text(ax, 64, 59, 'fractions', 'autre', 's')
rows = [(48, '5', '5/1'), (38, '2', '2/1'), (28, '10', '10/1')]
for y, a, b in rows:
    text(ax, 17, y, a, 'sujet', 'l')
    text(ax, 68, y, b, 'autre', 'l')
    arrow(ax, (24, y), (53, y), 'varie')
text(ax, 38, 52.5, 'plongement', 'varie', 's')
text(ax, 64, 17, '2/3 : nouveau', 'resultat', 's')
text(ax, 44, 6, r'$5\times2=10$ et $5/1\times2/1=10/1$', 'fixe', 's')
save(fig, '54-004')
