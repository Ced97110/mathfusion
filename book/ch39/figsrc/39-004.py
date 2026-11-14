import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(46)
f = numberline(ax, 8, 78, 22, -2, 10, step=1, every=2, arrow_right=False)
for v in (0, 9):
    disc(ax, f(v), 22, 1.2, 'sujet')
text(ax, f(0), 28, r'$0^2=0$', 'sujet')
text(ax, f(9), 28, r'$3^2=9$', 'sujet')
text(ax, f(9), 33, r'$(-3)^2=9$', 'sujet')
c = f(-1)
line(ax, [(c - 1.6, 22 - 1.6), (c + 1.6, 22 + 1.6)], 'limite', lw=1.4)
line(ax, [(c - 1.6, 22 + 1.6), (c + 1.6, 22 - 1.6)], 'limite', lw=1.4)
text(ax, c + 2, 38, r'$x^2=-1\ ?$', 'limite')
brace(ax, f(-2), f(0), 16, 'limite', label='aucun carré ici', down=True)
save(fig, '39-004')
