import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
xs = [9, 33, 57, 79]
for x, w, r in zip(xs, ['000', '100', '110', '111'], ['sujet', 'sujet', 'varie', 'varie']):
    disc(ax, x, 28, 5.2, r, label=w, size='s')
arrow(ax, (xs[0] + 5.7, 28), (xs[1] - 5.7, 28), 'fixe')
arrow(ax, (xs[1] + 5.7, 28), (xs[2] - 5.7, 28), 'fixe')
arrow(ax, (xs[2] + 5.7, 28), (xs[3] - 5.7, 28), 'limite', lw=1.4)
text(ax, 21, 35, 'erreur 1', 'fixe', 's')
text(ax, 45, 35, 'erreur 2', 'fixe', 's')
text(ax, 68, 36, 'correction\nà tort', 'limite', 's')
text(ax, 9, 18.5, 'envoyé', 'sujet', 's')
text(ax, 57, 18.5, 'reçu', 'varie', 's')
text(ax, 79, 18.5, 'corrigé', 'limite', 's')
text(ax, 44, 6, 'le récepteur ne sait pas qu’il se trompe', 'limite', 's')
save(fig, '68-019')
