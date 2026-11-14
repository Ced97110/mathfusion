import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'lattice', 'encre', 'l', weight='bold')
arrow(ax, (38, 53), (24, 47), 'fixe'); arrow(ax, (50, 53), (64, 47), 'fixe')
for i in range(3):
    for j in range(3): disc(ax, 14 + 8*i, 28 + 8*j, 1.1, 'sujet')
nodes = [(66, 28), (58, 36), (74, 36), (66, 44)]
for a, b in [(0, 1), (0, 2), (1, 3), (2, 3)]: line(ax, [nodes[a], nodes[b]], 'autre', lw=1.0)
for n in nodes: disc(ax, *n, 1.4, 'autre')
text(ax, 22, 18, 'réseau', 'sujet', 'l'); text(ax, 22, 12, 'grille de points', 'sujet', 's'); text(ax, 22, 6, 'chapitre 74', 'sujet', 's')
text(ax, 66, 18, 'treillis', 'autre', 'l'); text(ax, 66, 12, 'ensemble ordonné', 'autre', 's'); text(ax, 66, 6, 'chapitre 79', 'autre', 's')
save(fig, '74-073')
