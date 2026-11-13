import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
y = 22
f = numberline(ax, 32, 76, y, 0, 4, arrow_right=True)
disc(ax, 10, y, 4.5, 'sujet', label=r'$-\infty$', size='s')
line(ax, [(15.5, y), (30, y)], 'sujet', dash=True)
text(ax, 10, 33, 'polynôme nul', 'sujet', 's')
text(ax, 56, 33, 'polynômes non nuls : degrés', 'fixe', 's')
text(ax, 44, 7, 'plus petit que tout entier', 'sujet', 'm')
save(fig, '54-127')
