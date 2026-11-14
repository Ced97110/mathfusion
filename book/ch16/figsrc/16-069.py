import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
f = numberline(ax, 10, 70, 14, 0, 6)
box(ax, f(0), 24, f(3) - f(0), 7, 'sujet', label=r'$x$')
box(ax, f(3), 24, f(6) - f(3), 7, 'sujet', label=r'$x$')
brace(ax, f(0), f(6), 34, 'varie', label=r'2 fois la longueur $x$', down=False)
disc(ax, f(6), 14, 2.2, 'resultat')
line(ax, [(f(6), 24), (f(6), 16.5)], 'resultat', dash=True)
save(fig, '16-069')
