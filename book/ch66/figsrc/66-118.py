import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, 'paquet 1 : 27 polynômes', 'sujet', 'm')
for r in range(3):
    for c in range(9):
        x, y = 4 + 9.2 * c, 42 + 5.6 * r
        role = 'fixe' if (r == 0 and c == 0) else 'sujet'
        poly(ax, [(x, y), (x + 8.2, y), (x + 8.2, y + 4.6), (x, y + 4.6)], role)
text(ax, 8.1, 44.3, 'nul', 'fixe', 's')
brace(ax, 4, 86.8, 41, 'varie', label='26 × 2 = 52 racines au plus')
arrow(ax, (20, 31), (20, 25.5), 'varie')
box(ax, 4, 14, 34, 11, 'resultat', label='racines du paquet 1', size='s')
box(ax, 38, 14, 24, 11, 'resultat', label='paquet 2', size='s')
box(ax, 62, 14, 16, 11, 'resultat', label='paquet 3', size='s')
box(ax, 78, 14, 8, 11, 'resultat', label='…', size='s')
arrow(ax, (4, 8), (84, 8), 'varie')
text(ax, 44, 3, 'une seule liste, paquet après paquet', 'resultat', 's')
save(fig, '66-118')
