import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
xs = [10 + 17 * i for i in range(5)]
for i, x in enumerate(xs):
    n = i + 1
    box(ax, x - 5, 18, 10, 13, 'sujet' if n in (2, 4) else 'fixe', label=str(n), size='l')
arrow(ax, (xs[1], 32.5), (xs[3], 32.5), 'varie', curve=-0.3, both=True)
text(ax, xs[2], 42, 'échange', 'varie', 's')
text(ax, 44, 13, '1, 3 et 5 ne bougent pas', 'fixe', 's')
text(ax, 44, 5, 'transposition (2 4)', 'sujet', 'm')
save(fig, '46-193')
