import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 6, 76, 20, -96, 96, step=32, labels=True)
box(ax, f(0), 24, f(64) - f(0), 7, 'resultat', label='carrés : toujours ≥ 0', size='s')
disc(ax, f(-64), 20, 1.8, 'limite')
text(ax, f(-64), 27.5, 'x² = −64 ?', 'limite', 's')
text(ax, 44, 8, 'aucun carré ne vaut −64', 'limite', 's')
save(fig, '23-040')
