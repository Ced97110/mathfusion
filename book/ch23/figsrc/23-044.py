import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, '(x + p)² = x² + 2px + p²', 'sujet', 'm')
text(ax, 43, 50, 'double de p', 'varie', 's'); text(ax, 73, 50, 'carré de p', 'resultat', 's')
for y, p, m, l in ((34, 1, '2x', '1'), (21, 3, '6x', '9'), (8, 5, '10x', '25')):
    box(ax, 4, y, 20, 10, 'fixe', label=f'p = {p}')
    box(ax, 30, y, 26, 10, 'varie', label=m)
    box(ax, 62, y, 22, 10, 'resultat', label=l)
save(fig, '23-044')
