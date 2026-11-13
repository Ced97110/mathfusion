import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 24
f = numberline(ax, 10, 66, y, 0, 4, step=1, labels=False)
for v in (3, 4): text(ax, f(v), y - 5, '1 000 00' + str(v - 3), 'fixe', 's')
disc(ax, f(3), y, 2.2, 'sujet'); disc(ax, f(4), y, 2.2, 'limite')
text(ax, f(3), y + 6, r'$N$', 'sujet', 'm'); text(ax, f(4), y + 6, r'$N + 1$', 'limite', 'm')
arrow(ax, (f(3) + 1, y + 11), (f(4) - 1, y + 11), 'varie', curve=-0.4)
text(ax, (f(3) + f(4)) / 2, y + 17, '+ 1', 'varie', 's')
text(ax, 44, 50, r'$N$ serait le plus grand ?', 'sujet', 'm')
box(ax, 10, 2, 68, 8, 'limite', label=r'impossible : $N + 1 > N$', size='s')
save(fig, '42-100')
