import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, 'test des produits en croix', 'encre', 's')
panels = [(0, '(2, 4)', r'$1\times4=4$', r'$2\times2=4$', 'resultat', 'équivalents'),
          (44, '(2, 5)', r'$1\times5=5$', r'$2\times2=4$', 'limite', 'différents')]
for dx, c2, p1, p2, role, verdict in panels:
    box(ax, 4 + dx, 48, 17, 10, 'sujet', label='(1, 2)', size='s')
    box(ax, 23 + dx, 48, 17, 10, 'autre', label=c2, size='s')
    text(ax, 22 + dx, 40, p1, 'varie', 's')
    text(ax, 22 + dx, 33, p2, 'varie', 's')
    arrow(ax, (22 + dx, 30), (22 + dx, 25), 'varie')
    box(ax, 5 + dx, 14, 34, 11, role, label=verdict, size='s')
save(fig, '54-017')
