import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
box(ax, 7, 8, 30, 12, 'fixe', label='ℚ', size='m'); box(ax, 7, 36, 30, 12, 'fixe', label='ℚ (inchangé)', size='s')
arrow(ax, (22, 20), (22, 36), 'fixe')
text(ax, 25, 28, '+ √9 = 3', 'fixe', 's', ha='left'); text(ax, 19, 28, 'degré 1', 'fixe', 's', ha='right')
box(ax, 51, 8, 30, 12, 'fixe', label='ℚ', size='m'); box(ax, 51, 36, 30, 12, 'sujet', label='ℚ(√2)', size='m')
arrow(ax, (66, 20), (66, 36), 'varie')
text(ax, 69, 28, '+ √2', 'varie', 's', ha='left'); text(ax, 63, 28, 'degré 2', 'varie', 's', ha='right')
save(fig, '61-156')
