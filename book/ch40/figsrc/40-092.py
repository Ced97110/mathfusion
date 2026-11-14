import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 4, 69, 't = 0 : (x ; y) = (4 ; 0)', 'encre', 's', ha='left')
text(ax, 4, 63, 'quart de tour : (x ; y) = (0 ; 4)', 'encre', 's', ha='left')
box(ax, 3, 22, 18, 12, 'varie', label='t (temps)', size='s')
box(ax, 42, 40, 42, 10, 'sujet', label='x = 4 cos t', size='m')
box(ax, 42, 6, 42, 10, 'sujet', label='y = 4 sin t', size='m')
arrow(ax, (21, 31), (42, 43), 'varie')
arrow(ax, (21, 25), (42, 13), 'varie')
text(ax, 31, 44, 'règle f', 'varie', 's') if False else None
# x ne commande pas y
line(ax, [(63, 39), (63, 17)], 'limite', lw=1.0, dash=True)
text(ax, 63, 28, '×', 'limite', 'l', weight='bold')
text(ax, 70, 28, 'aucun ordre', 'limite', 's', ha='left')
save(fig, '40-092')
