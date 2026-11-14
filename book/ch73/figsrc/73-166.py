import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$F_2=\{0,1\}$', 'encre', 'l')
disc(ax, 24, 44, 5, 'fixe', label='0', size='l'); disc(ax, 64, 44, 5, 'sujet', label='1', size='l')
text(ax, 24, 34, 'nul : exclu', 'fixe', 's'); text(ax, 64, 34, 'seul d possible', 'sujet', 's')
arrow(ax, (64, 38.5), (64, 26), 'varie')
box(ax, 34, 12, 52, 13, 'limite', label='')
text(ax, 60, 21, r'$1\times 1=1$', 'limite', 'm'); text(ax, 60, 15, 'échec : d² = 1', 'limite', 's')
save(fig, '73-166')
