import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
box(ax, 8, 72, 72, 9, 'fixe', label='produit 12 : même signe', size='s')
box(ax, 8, 61, 72, 9, 'fixe', label=r'somme $-7$ : deux négatifs', size='s')
rows = [(r'$-1$ et $-12$', r'$-13$', 'limite'), (r'$-2$ et $-6$', r'$-8$', 'limite'), (r'$-3$ et $-4$', r'$-7$', 'resultat')]
for k, (c, s, r) in enumerate(rows):
    y = 44 - 13 * k
    box(ax, 8, y, 34, 10, 'sujet', label=c)
    arrow(ax, (42, y + 5), (52, y + 5), 'varie')
    box(ax, 52, y, 22, 10, r, label=s)
arrow(ax, (63, 18), (60, 13.3), 'resultat')
box(ax, 22, 3, 44, 10, 'resultat', label=r'$(x-3)(x-4)$')
save(fig, '18-073')
