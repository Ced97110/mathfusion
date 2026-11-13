import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 14, 72, 'paires', 'sujet', 'm'); text(ax, 74, 72, 'impaires', 'autre', 'm')
text(ax, 44, 72, r'$(1\ 2)\tau$', 'varie', 'm')
L = ['id', '(1 2 3)', '(1 3 2)']; R = ['(1 2)', '(2 3)', '(1 3)']
for i in range(3):
    y = 52 - i * 17
    box(ax, 2, y - 5, 24, 10, 'sujet', label=L[i], size='s')
    box(ax, 62, y - 5, 24, 10, 'autre', label=R[i], size='s')
    arrow(ax, (27, y), (61, y), 'varie')
text(ax, 44, 4, 'un à un : rien perdu, rien doublé', 'resultat', 'm')
save(fig, '46-232')
