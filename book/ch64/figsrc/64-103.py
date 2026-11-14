import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 23, 80, 'K et G/K résolubles', 'resultat', 's')
text(ax, 65, 80, 'K non résoluble', 'limite', 's')
cols = [(2, [('K\nrésoluble', 'resultat'), ('G/K\nrésoluble', 'resultat'), ('G\nrésoluble', 'resultat')]),
        (46, [(r'$K=A_5$ (60)' + '\nnon résoluble', 'limite'), (r'$S_5/A_5$ (2)' + '\nrésoluble', 'resultat'), (r'$G=S_5$ (120)' + '\nnon résoluble', 'limite')])]
for x0, items in cols:
    (a, ra), (b, rb), (g, rg) = items
    box(ax, x0, 52, 19, 16, ra, label=a, size='s')
    box(ax, x0 + 21, 52, 19, 16, rb, label=b, size='s')
    box(ax, x0 + 10.5, 14, 19, 16, rg, label=g, size='s')
    arrow(ax, (x0 + 9.5, 51), (x0 + 16, 31.5), 'fixe')
    arrow(ax, (x0 + 30.5, 51), (x0 + 24, 31.5), 'fixe')
save(fig, '64-103')
