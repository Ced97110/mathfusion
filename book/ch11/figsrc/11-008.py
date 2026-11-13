import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cells = [(i, j, k) for i in range(5) for j in range(2) for k in range(2)]
cubes(ax, cells, (14, 7), 5.0, 'sujet')
text(ax, 25, 56, '5 × 2 × 2 cm', 'sujet', 'm')
text(ax, 25, 2.5, '20 cubes remplissent la boîte', 'resultat', 's')
cubes(ax, [(0, 0, 0)], (68, 26), 8.0, 'varie')
text(ax, 68, 48, '1 cube étalon', 'varie', 's')
text(ax, 68, 17, "arête : 1 cm", 'varie', 's')
save(fig, '11-008')
