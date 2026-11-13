import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 73, r'radical : zéro avec tout vecteur', 'encre', 's')
box(ax, 2, 40, 28, 14, 'sujet', label=r'$(0,0,1)$', size='m')
for i, t in enumerate(['avec (3, 4, 5) : 0', 'avec (1, 1, 1) : 0', 'avec tout autre : 0']):
    y = 56 - i*14
    box(ax, 52, y, 34, 10, 'resultat', label=t, size='s'); arrow(ax, (31, 47), (51, y + 5), 'varie', lw=0.9)
text(ax, 16, 35, 'dans le radical :', 'limite', 's'); text(ax, 16, 29, 'dégénérée', 'limite', 's')
line(ax, [(2, 22), (86, 22)], 'fixe', lw=0.5, dash=True)
box(ax, 2, 4, 34, 13, 'autre', label='plan habituel', size='s')
box(ax, 44, 4, 42, 13, 'resultat', label='radical = 0 :\nnon dégénérée', size='s'); arrow(ax, (37, 10.5), (43, 10.5), 'varie', lw=0.9)
save(fig, '72-032')
