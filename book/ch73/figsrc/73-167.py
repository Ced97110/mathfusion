import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$F_3=\{0,1,2\}$', 'encre', 'l')
for x, l, r in [(18, '0', 'fixe'), (44, '1', 'sujet'), (70, '2', 'sujet')]:
    disc(ax, x, 50, 5, r, label=l, size='l')
text(ax, 18, 41, 'nul : exclu', 'fixe', 's')
text(ax, 44, 41, r'$1^2=1$', 'varie', 's'); text(ax, 70, 41, r'$2^2=4\equiv 1$', 'varie', 's')
arrow(ax, (44, 38), (50, 25), 'varie'); arrow(ax, (70, 38), (66, 25), 'varie')
box(ax, 32, 12, 52, 12, 'limite', label='carré = 1 : échec', size='s')
save(fig, '73-167')
