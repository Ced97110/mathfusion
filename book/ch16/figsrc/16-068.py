import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
f = numberline(ax, 14, 74, 16, 0, 6)
disc(ax, f(0), 16, 2.4, 'sujet'); disc(ax, f(6), 16, 2.4, 'sujet')
text(ax, f(0), 34, r'$O$', 'sujet', 'xl'); text(ax, f(6), 34, r'$P$', 'sujet', 'xl')
text(ax, f(0), 27, 'le point de 0', 'fixe', 's'); text(ax, f(6), 27, 'le point de 6', 'fixe', 's')
arrow(ax, (f(0), 31), (f(0), 19), 'fixe', lw=0.6); arrow(ax, (f(6), 31), (f(6), 19), 'fixe', lw=0.6)
save(fig, '16-068')
