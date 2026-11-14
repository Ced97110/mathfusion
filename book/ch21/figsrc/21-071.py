import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 14, 44, 60, 11, 'resultat', label=r'PPCM $=(x-1)^2(x+3)$')
box(ax, 10, 22, 16, 9, 'sujet', label=r'$x-1$'); box(ax, 28, 22, 16, 9, 'sujet', label=r'$x-1$')
box(ax, 52, 22, 16, 9, 'autre', label=r'$x+3$')
arrow(ax, (27, 32), (27, 43), 'varie'); arrow(ax, (60, 32), (60, 43), 'varie')
text(ax, 27, 16, r'$D_1$ : 2 fois, $D_2$ : 1', 'sujet', 's'); text(ax, 62, 10, r'seulement dans $D_2$', 'autre', 's')
save(fig, '21-071')
