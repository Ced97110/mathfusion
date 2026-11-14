import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
y = 18
f = numberline(ax, 6, 64, y, -5, 5, every=5, arrow_right=False)
box(ax, f(-5) - 2, y + 5, f(0) - f(-5) - 2, 9, 'fixe', label='à gauche', size='s')
box(ax, f(0) + 2, y + 5, f(5) - f(0), 9, 'sujet', label='à droite : positifs', size='s')
line(ax, [(f(0), y), (f(5), y)], 'sujet', lw=2.2)
disc(ax, f(5), y, 1.7, 'sujet'); disc(ax, f(-5), y, 1.7, 'limite'); disc(ax, f(0), y, 1.5, 'fixe')
text(ax, f(5), y + 17, 'positif', 'sujet', 's')
text(ax, f(-5), y + 17, 'non positif', 'limite', 's')
text(ax, f(0), y - 11, '0 : non positif', 'fixe', 's')
save(fig, '13-020')
