import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
box(ax, 2, 44, 84, 14, 'limite', label='e × d = 3 × 5 = 15\nreste 15 par 40, pas 1')
box(ax, 2, 22, 14, 12, 'sujet', label='8')
box(ax, 34, 22, 14, 12, 'fixe', label='17')
box(ax, 66, 22, 14, 12, 'limite', label='32')
arrow(ax, (16.5, 28), (33.5, 28), 'varie'); arrow(ax, (48.5, 28), (65.5, 28), 'varie')
text(ax, 25, 32, 'puissance 3', 'varie', 's')
text(ax, 57, 32, 'puissance 5', 'varie', 's')
text(ax, 73, 17, '≠', 'limite', 'l')
box(ax, 58, 2, 28, 10, 'sujet', label='attendu : 8', dash=True, fill=False)
save(fig, '53-136')
