import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'écrit en entier, trois fois', 'fixe', 's')
for i in range(3): box(ax, 2 + 29 * i, 40, 26, 11, 'sujet', label=r'$x(x-1)$', size='s')
arrow(ax, (44, 38), (44, 26), 'varie')
text(ax, 66, 32, r'$M=x(x-1)$', 'varie', 's')
for c in (15, 44, 73): box(ax, c - 7, 13, 14, 11, 'sujet', label='$M$', size='m')
text(ax, 44, 5, 'écrit avec une lettre', 'fixe', 's')
save(fig, '21-121')
