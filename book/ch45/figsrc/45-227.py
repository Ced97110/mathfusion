import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 70, 'deux groupes, 4 éléments chacun', 'encre', 'm', weight='bold')
box(ax, 2, 22, 40, 42, 'sujet', fill=True)
box(ax, 46, 22, 40, 42, 'autre', fill=True)
text(ax, 22, 59, r'horloge $\mathbb{Z}/4$', 'sujet', 'm')
text(ax, 66, 59, 'rectangle', 'autre', 'm')
for k in range(4):
    a = math.radians(90 - 90 * k); x, y = 22 + 10 * math.cos(a), 42 + 10 * math.sin(a)
    disc(ax, x, y, 3.2, 'sujet', label=str(k), size='s')
arrow(ax, (22 + 3.5, 52), (32, 42 + 3.5), 'varie', curve=-0.2)
text(ax, 22, 28, r'$1+1=2\neq0$', 'varie', 'm')
rx, ry = 66, 43
poly(ax, [(rx - 11, ry - 6), (rx + 11, ry - 6), (rx + 11, ry + 6), (rx - 11, ry + 6)], 'autre')
text(ax, 66, 28, r'$h^2=v^2=d^2=e$', 'autre', 'm')
box(ax, 8, 4, 72, 12, 'limite', label='même taille, pas isomorphes', size='m')
save(fig, '45-227')
