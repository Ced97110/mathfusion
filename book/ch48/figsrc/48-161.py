import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
heads = [(16, r'$H$ : 3', 'sujet', [0, 4, 8]), (44, r'$N$ : 2', 'autre', [0, 6]), (72, r'$H\cap N$ : 1', 'fixe', [0])]
for cx, t, role, els in heads:
    text(ax, cx, 66, t, role, 'm')
    n = len(els)
    for i, e in enumerate(els):
        x = cx + (i - (n - 1) / 2) * 8.5
        disc(ax, x, 56, 3.2, role, label=str(e), size='s')
box(ax, 6, 28, 50, 9, 'varie', label=r'$3 \times 2 = 6$')
box(ax, 6, 8, 74, 9, 'resultat', label=r'$6 \div 1 = 6$ éléments dans $HN$', size='m')
arrow(ax, (16, 52.5), (16, 37.8), 'fixe'); arrow(ax, (44, 52.5), (44, 37.8), 'fixe')
arrow(ax, (31, 28), (31, 17.8), 'varie')
arrow(ax, (72, 52.5), (72, 17.8), 'fixe')
save(fig, '48-161')
