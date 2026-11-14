import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 70, 20, 0, 5)
disc(ax, f(3), 20, 3.2, 'sujet', label=r'$P$', size='s')
text(ax, 44, 44, r'$a=3$', 'sujet', 'xl')
arrow(ax, (f(3), 38), (f(3), 24.5), 'sujet')
text(ax, 20, 36, 'a = le nombre sous P', 'sujet', 's')
save(fig, '13-011')
