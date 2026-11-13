import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
k = 0.37
box(ax, 6, 36, 203 * k, 12, 'fixe'); box(ax, 6, 36, 97.44 * k, 12, 'sujet', label='48 % : 97,44', size='s')
text(ax, 6 + 203 * k / 2, 52, '203', 'fixe', 'm')
box(ax, 6, 8, 200 * k, 12, 'fixe'); box(ax, 6, 8, 100 * k, 12, 'varie', label='50 % : 100', size='s')
text(ax, 6 + 200 * k / 2, 24, '200', 'fixe', 'm')
arrow(ax, (44, 35), (44, 29), 'varie'); text(ax, 62, 32, 'on arrondit', 'varie', 's')
save(fig, '09-122')
