import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 62, 'restes par 6', 'fixe', 's')
for i in range(6):
    box(ax, 5.75 + i * 13, 44, 11.5, 11, 'varie' if i in (2, 3) else 'fixe', label=r'$\bar{%d}$' % i)
box(ax, 22, 18, 44, 12, 'limite', label=r'$\bar2\times\bar3=\bar0$')
arrow(ax, (37.5, 44), (40, 30.5), 'varie'); arrow(ax, (50.5, 44), (48, 30.5), 'varie')
text(ax, 44, 9, r'donc (6) n’est pas premier', 'limite', 's')
save(fig, '52-126')
