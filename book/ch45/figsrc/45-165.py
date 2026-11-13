import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 15.5, 62, 'G (interrupteur)', 'fixe'); text(ax, 61.5, 62, 'H (cadran)', 'fixe')
for i in range(2): box(ax, 4 + 12 * i, 49, 11, 9, 'fixe', label=str(i))
for i in range(3): box(ax, 44 + 12 * i, 49, 11, 9, 'fixe', label=str(i))
text(ax, 35.5, 53.5, 'côte à côte', 'fixe', 's')
arrow(ax, (15.5, 47), (32, 33), 'varie'); arrow(ax, (61.5, 47), (56, 33), 'varie')
for r in range(2):
    for c in range(3): box(ax, 29 + 10 * c, 16 + 9 * r, 10, 9, 'sujet')
text(ax, 44, 10, r'groupe nouveau $G\times H$', 'sujet')
save(fig, '45-165')
