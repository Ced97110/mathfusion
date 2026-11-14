import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
y = 28; x0, x1 = 6, 76
f = numberline(ax, x0, x1, y, 3000, 8000, 500, labels=False)
disc(ax, f(4100), y, 2.4, 'sujet', label='1'); disc(ax, f(7050), y, 2.4, 'varie', label='2')
text(ax, f(4100), y + 8, 'attendu 4 100 (avant)', 'sujet', 'm', ha='center')
text(ax, f(7050), y + 8, 'écran 7 050 (après)', 'varie', 'm', ha='center')
arrow(ax, (f(4100) + 3, y - 5), (f(7050) - 3, y - 5), 'fixe', both=True)
text(ax, (f(4100) + f(7050)) / 2, y - 10, '3 : comparer, écart 2 950', 'fixe', 'm')
save(fig, '10-007')
