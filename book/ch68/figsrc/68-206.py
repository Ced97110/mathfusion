import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(90)
text(ax, 44, 84, r'le code s’annule en $\alpha$ et $\alpha^2$', 'varie', 'm')
xs, p = brow(fig, ax, 44, 74, '0123456', roles=['varie' if i in (1, 2) else 'fixe' for i in range(7)])
brace(ax, xs[1] - p / 2, xs[2] + p / 2, 69, 'varie', r'$s = 2$ puissances de suite')
text(ax, 44, 52, 'poids d’un mot non nul', 'fixe', 's')
f = numberline(ax, 10, 70, 28, 0, 5, size='m')
disc(ax, f(1), 28, 2.4, 'limite', fill=False)
disc(ax, f(2), 28, 2.4, 'limite', fill=False)
disc(ax, f(3), 28, 2.4, 'resultat')
text(ax, (f(1) + f(2)) / 2, 36, 'aucun mot', 'limite', 's')
arrow(ax, (f(3), 33), (f(5) + 3, 33), 'resultat')
text(ax, f(4), 39, r'$d \geq 3 = s + 1$', 'resultat', 's')
save(fig, '68-206')
