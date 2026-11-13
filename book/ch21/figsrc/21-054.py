import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
y = 40
f = numberline(ax, 8, 70, y, 0, 8, labels=False)
disc(ax, f(3), y, 2.4, 'autre', label='b', size='s')
disc(ax, f(7), y, 2.4, 'sujet', label='a', size='s')
arrow(ax, (f(3), y + 2.6), (f(7), y + 2.6), 'varie', curve=-0.4)
text(ax, (f(3) + f(7)) / 2, y + 12, r'$a-b=4$', 'varie', 'm')
arrow(ax, (f(7), y - 2.6), (f(3), y - 2.6), 'varie', curve=-0.4)
text(ax, (f(3) + f(7)) / 2, y - 12, r'$b-a=-4$', 'varie', 'm')
text(ax, 4, 66, 'a = 7', 'sujet', 's', ha='left')
text(ax, 24, 66, 'b = 3', 'autre', 's', ha='left')
box(ax, 22, 6, 44, 13, 'resultat', label=r'$\frac{4}{-4}=-1$', size='l')
save(fig, '21-054')
