import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 8, 74, 24, -3, 3, 1)
disc(ax, f(3), 24, 1.7, 'sujet'); disc(ax, f(-3), 24, 1.7, 'varie'); disc(ax, f(0), 24, 1.7, 'resultat')
arrow(ax, (f(3), 27), (f(-3), 27), 'varie', curve=0.7)
text(ax, 44, 58, '3 devient −3', 'varie', 'm')
box(ax, 33, 33, 22, 8, 'resultat', label='−0 = 0', size='m')
text(ax, 44, 9, '0 reste sur 0', 'resultat', 's')
save(fig, '13-126')
