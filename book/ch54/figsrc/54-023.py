import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, 'même reste = même groupe', 'encre', 's')
groups = [(4, 'fixe', 'reste 0', '3, 6, 9'), (31, 'sujet', 'reste 1', '1, 4, 7, 10'), (58, 'fixe', 'reste 2', '2, 5, 8')]
for x, role, h, nums in groups:
    box(ax, x, 34, 26, 22, role)
    text(ax, x + 13, 50, h, role, 's')
    text(ax, x + 13, 42, nums, role, 'm')
arrow(ax, (40, 34), (34, 24.5), 'varie')
arrow(ax, (48, 34), (54, 24.5), 'varie')
box(ax, 26, 14, 14, 10, 'varie', label='1', size='l')
box(ax, 48, 14, 14, 10, 'varie', label='4', size='l')
text(ax, 44, 19, 'ou', 'varie', 's')
text(ax, 44, 6, 'on nomme le groupe par un membre', 'varie', 's')
save(fig, '54-023')
