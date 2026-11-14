import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 38, 75, r'3 classes de $H$ (3 lignes)', 'sujet', 'm')
rows = [[(0, 6), (3, 9)], [(1, 7), (4, 10)], [(2, 8), (5, 11)]]
for r, pieces in enumerate(rows):
    y = 55 - r * 17
    box(ax, 3, y - 2, 56, 14, 'sujet', fill=False)
    for k, (a, b) in enumerate(pieces):
        box(ax, 5 + k * 27, y, 25, 10, 'autre', label=f'{a}, {b}', size='s')
    text(ax, 70, y + 5, r'$\times2$', 'autre', 'm')
text(ax, 70, 68, 'morceaux', 'autre', 's')
text(ax, 44, 12, r'$3\times2=6$ classes de $K$', 'resultat', 'm')
text(ax, 44, 4.5, r'$K=\{0,6\}$ : 2 éléments par morceau', 'autre', 's')
save(fig, '47-091')
