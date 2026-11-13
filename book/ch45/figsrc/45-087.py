import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 54, r'$a=3$, $b=2$, $x=1$', 'encre', 'm')
xs = [14, 44, 74]; y = 36
for x, n, r in zip(xs, ['1', '3', '2'], ['sujet', 'fixe', 'resultat']): disc(ax, x, y, 5, r, label=n)
text(ax, 14, 46, r'$x$', 'sujet', 'm'); text(ax, 44, 46, r'$bx$', 'fixe', 'm'); text(ax, 70, 46, r'$a(bx)=(ab)x$', 'resultat', 'm')
arrow(ax, (19.5, y), (38.5, y), 'varie'); arrow(ax, (49.5, y), (68.5, y), 'varie')
text(ax, 29, y + 4, r'$b_L$', 'varie', 'm'); text(ax, 59, y + 4, r'$a_L$', 'varie', 'm')
arrow(ax, (14, y - 5.5), (74, y - 5.5), 'autre', curve=0.35)
text(ax, 44, 14, r'$(ab)_L$', 'autre', 'm')
text(ax, 44, 6, 'associativité : même arrivée', 'encre', 's')
save(fig, '45-087')
