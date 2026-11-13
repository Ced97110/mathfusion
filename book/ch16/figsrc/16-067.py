import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
f = numberline(ax, 10, 70, 18, 0, 6)
box(ax, f(0), 28, f(3) - f(0), 7, 'sujet', label=r'$x$')
box(ax, f(3), 28, f(6) - f(3), 7, 'resultat', label=r'$x$')
line(ax, [(f(3), 28), (f(3), 18)], 'fixe', dash=True)
line(ax, [(f(6), 28), (f(6), 18)], 'fixe', dash=True)
text(ax, f(0), 40, r'$O$', 'encre', 'l'); text(ax, f(6), 40, r'$P$', 'encre', 'l')
save(fig, '16-067')
