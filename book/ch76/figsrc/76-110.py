import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 6, 76, 26, 0, 6, arrow_right=False)
arrow(ax, (f(1), 30), (f(2), 30), 'varie', curve=-0.5); text(ax, f(1.5), 37, r'$B$ : $\times2$', 'varie', 's')
arrow(ax, (f(2), 30), (f(6), 30), 'autre', curve=-0.3); text(ax, f(4), 41, r'$A$ : $\times3$', 'autre', 's')
disc(ax, f(5), 26, 1.6, 'limite'); disc(ax, f(6), 26, 1.6, 'resultat')
text(ax, f(5) + 3, 15, r'$2+3=5$ : faux', 'limite', 's', ha='right')
text(ax, f(6) + 4, 8, r'$2\times3=6=\det(AB)$', 'resultat', 's', ha='right')
save(fig, '76-110')
