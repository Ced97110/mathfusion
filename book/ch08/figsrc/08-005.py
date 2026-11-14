import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, '2 mètres et 35 centièmes', 'encre', 'm')
xs = [13, 35, 57]
for x, d in zip(xs, '235'):
    box(ax, x, 28, 18, 16, 'sujet', label=d, size='xl')
    box(ax, x + 4, 48, 10, 10, 'varie', label='?', size='l')
    arrow(ax, (x + 9, 47.5), (x + 9, 44.5), 'varie')
arrow(ax, (44, 27), (44, 17), 'limite')
box(ax, 13, 4, 62, 12, 'limite', label='235 se lit 235 mètres', size='m')
save(fig, '08-005')
