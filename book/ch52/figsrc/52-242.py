import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for x, s in [(2, '2 par 3'), (31, '0 par 4'), (60, '1 par 5')]:
    box(ax, x, 62, 26, 9, 'sujet', label=s)
box(ax, 12.5, 38, 34, 9, 'varie', label='8 (à 12 près)')
box(ax, 31, 10, 40, 9, 'resultat', label='56 (à 60 près)')
arrow(ax, (15, 62), (23, 47), 'varie')
arrow(ax, (44, 62), (36, 47), 'varie')
arrow(ax, (29.5, 38), (42, 19), 'varie')
arrow(ax, (73, 62), (60, 19), 'varie')
text(ax, 2, 54, 'fusion 1', 'varie', 's', ha='left')
text(ax, 2, 28, 'fusion 2', 'varie', 's', ha='left')
save(fig, '52-242')
