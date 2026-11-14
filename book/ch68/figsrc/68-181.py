import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(66)
box(ax, 2, 38, 34, 18, 'sujet', label='messages\n4 bits, degré ≤ 3', size='s')
box(ax, 50, 38, 36, 18, 'resultat', label='multiples de g\n7 bits, degré ≤ 6', size='s')
arrow(ax, (37, 52), (49, 52), 'varie')
text(ax, 43, 56, r'$\times\ g$', 'varie', 'm')
arrow(ax, (49, 42), (37, 42), 'varie')
text(ax, 43, 37.5, r'$\div\ g$', 'varie', 'm')
brow(fig, ax, 19, 22, '1001', role='sujet', size='m')
brow(fig, ax, 67, 22, '1100101', role='resultat', size='m')
arrow(ax, (31.5, 22), (45.5, 22), 'varie')
text(ax, 44, 8, 'même ensemble des deux côtés', 'encre', 's')
save(fig, '68-181')
