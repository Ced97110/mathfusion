import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 2, 38, 84, 22, 'fixe', fill=False, dash=True)
text(ax, 44, 56, 'une classe : un seul nombre', 'fixe', 's')
xs = [8, 34, 60]
for x, t, k in zip(xs, ['3/4', '6/8', '9/12'], '123'):
    box(ax, x, 41, 20, 9, 'resultat' if t == '3/4' else 'fixe', label=t, size='m')
    arrow(ax, (x + 10, 61), (x + 10, 70), 'limite')
    disc(ax, x + 10, 74, 3.2, 'limite', label=k, size='s')
text(ax, 44, 81, 'trois numéros', 'limite', 's')
arrow(ax, (18, 40), (18, 20), 'resultat')
disc(ax, 18, 15.5, 3.2, 'resultat', label='1', size='s')
text(ax, 58, 28, 'le représentant : 3/4', 'resultat', 's')
text(ax, 58, 14, 'un seul numéro', 'resultat', 's')
save(fig, '43-136')
