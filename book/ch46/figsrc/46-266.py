import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 14, 84, 36, 'fixe', fill=False, dash=True)
text(ax, 8, 46, 'H', 'fixe', 'm')
xs = [10, 34, 58]
box(ax, xs[0], 24, 20, 12, 'sujet', label='$a = (1\\ 2\\ 3)$', size='s')
box(ax, xs[1], 24, 20, 12, 'autre', label='$a^2 = (1\\ 3\\ 2)$', size='s')
box(ax, xs[2], 24, 24, 12, 'resultat', label='$a^3 = (1)$', size='s')
for i in range(2):
    arrow(ax, (xs[i] + [20, 20][i] + 0.3, 30), (xs[i + 1] - 0.3, 30), 'varie')
    text(ax, xs[i] + 20 + 2, 38.5, '× a', 'varie', 's')
arrow(ax, (xs[2] + 12, 37), (xs[0] + 10, 37), 'fixe', lw=0.7, curve=0.28)
text(ax, 44, 55, 'la suite revient au neutre', 'fixe', 's')
text(ax, 44, 8, '$a^{-1} = a^{r-1} = a^2$ est dans H', 'autre', 's')
text(ax, 70, 19, '$r = 3$', 'resultat', 's')
save(fig, '46-266')
