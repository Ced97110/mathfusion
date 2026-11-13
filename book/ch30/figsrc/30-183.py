import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
tri = lambda x, y, r: poly(ax, [(x, y), (x + 5, y), (x, y + 5)], r)
for i in range(4): tri(3 + 6.5 * i, 27, 'sujet')
for i in range(3):
    for j in range(3): tri(33 + 7 * i, 20 + 7 * j, 'autre')
tri(70.5, 27, 'fixe')
arrow(ax, (3, 15), (27, 15), 'sujet', both=True)
arrow(ax, (33, 15), (52, 15), 'autre', both=True); arrow(ax, (55, 20), (55, 39), 'autre', both=True)
text(ax, 15, 46, 'Frise', 'sujet', 'l', weight='bold'); text(ax, 44, 46, 'Carrelage', 'autre', 'l', weight='bold'); text(ax, 73, 46, 'Dessin isolé', 'fixe', 'm', weight='bold')
text(ax, 15, 8, '1 direction', 'sujet', 's'); text(ax, 44, 8, '2 directions', 'autre', 's'); text(ax, 73, 8, 'aucune direction', 'fixe', 's')
save(fig, '30-183')
