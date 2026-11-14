import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(92)
box(ax, 6, 78, 76, 11, 'sujet', label='départ : idéal stable par ×x', size='s')
arrow(ax, (44, 77), (44, 67), 'varie')
box(ax, 6, 34, 76, 32, 'varie', fill=False)
text(ax, 44, 60, 'étape qui porte le poids', 'varie', 'm')
text(ax, 44, 53, '×x = décalage (règle x⁷ = 1)', 'varie', 's')
w = '1100101'
d = w[-1] + w[:-1]
brow(fig, ax, 25, 42, w, role='sujet', size='s', k=4, h=5.0)
brow(fig, ax, 63, 42, d, role='resultat', size='s', k=4, h=5.0)
arrow(ax, (44.5, 42), (47.5, 42), 'varie')
text(ax, 44, 47, '×x', 'varie', 's')
arrow(ax, (44, 33), (44, 25), 'varie')
box(ax, 6, 12, 76, 12, 'resultat', label='arrivée : stable par décalage', size='s')
save(fig, '68-189')
