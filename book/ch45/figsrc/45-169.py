import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 13, 58, 'complète', 'fixe', 's'); text(ax, 57, 58, 'plus courte', 'sujet', 's')
box(ax, 2, 44, 22, 10, 'fixe', label='ℤ/nℤ'); arrow(ax, (24.5, 49), (45.5, 49), 'varie'); text(ax, 35, 52.5, 'sans un ℤ', 'varie', 's')
box(ax, 46, 44, 22, 10, 'sujet', label='ℤ/n')
text(ax, 57, 38.5, '=', 'sujet', 'l')
box(ax, 46, 24, 22, 10, 'autre', label='ℤₙ'); text(ax, 71, 29, 'Judson', 'autre', 's', ha='left')
box(ax, 2, 4, 28, 10, 'fixe', label='ℤ/2ℤ × ℤ/3ℤ'); arrow(ax, (30.5, 9), (47.5, 9), 'varie'); box(ax, 48, 4, 28, 10, 'sujet', label='ℤ/2 × ℤ/3')
save(fig, '45-169')
