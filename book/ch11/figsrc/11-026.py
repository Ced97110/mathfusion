import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 22, 56, 44, 10, 'sujet', label='2 miles', size='m')
box(ax, 22, 32, 44, 10, 'varie', label='10 560 pieds', size='m')
box(ax, 22, 8, 44, 10, 'resultat', label='3 520 yards', size='m')
arrow(ax, (44, 56), (44, 42.5), 'varie'); text(ax, 52, 49, r'$\times$ 5 280', 'varie', 's', ha='left')
arrow(ax, (44, 32), (44, 18.5), 'varie'); text(ax, 52, 25, r'$\div$ 3', 'varie', 's', ha='left')
save(fig, '11-026')
