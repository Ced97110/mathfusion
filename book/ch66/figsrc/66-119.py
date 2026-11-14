import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
f = numberline(ax, 8, 70, 14, 1870, 1890, 5, arrow_right=False)
disc(ax, f(1873), 14, 1.4, 'resultat'); disc(ax, f(1882), 14, 1.4, 'resultat')
text(ax, f(1873), 21, 'e : preuve 1873', 'resultat', 's')
text(ax, f(1882), 21, 'π : preuve 1882', 'resultat', 's')
box(ax, 50, 28, 36, 14, 'fixe', fill=False, dash=True, label='e + π : aucune preuve', size='s')
save(fig, '66-119')
