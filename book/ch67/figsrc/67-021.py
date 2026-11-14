import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 4, 52, 80, 19, 'sujet', fill=False, dash=True)
for i, l in enumerate(['0', '1', r'$\alpha$', r'$\alpha+1$']):
    box(ax, 8 + i * 19.5, 56, 16, 12, 'sujet', label=l)
brace(ax, 4, 84, 52, 'sujet', label='4 éléments')
arrow(ax, (44, 43), (44, 33), 'varie')
box(ax, 14, 20, 60, 13, 'varie', label='ordre du corps = 4', size='m')
text(ax, 20, 9, 'corps d’ordre 4', 'varie', 's')
text(ax, 44, 9, '=', 'encre', 'm')
text(ax, 67, 9, 'corps à 4 éléments', 'sujet', 's')
save(fig, '67-021')
