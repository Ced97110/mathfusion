import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 12, 76, 28, 0, 3, labels=True, arrow_right=False, size='m')
text(ax, 44, 7, r'$k$ = nombre de réflexions', 'encre', 's')
for k, role in ((0, 'limite'), (1, 'limite'), (2, 'resultat')):
    disc(ax, f(k), 28, 2.2, role)
brace(ax, f(0), f(2), 36, 'fixe', label=r'au plus $n = 2$', down=False)
text(ax, (f(0) + f(1)) / 2, 18 + 0.5, 'trop peu', 'limite', 's') if False else None
text(ax, f(0.5), 19, 'trop peu', 'limite', 's')
arrow(ax, (f(2), 52), (f(2), 31), 'resultat')
box(ax, f(2) - 17, 52, 34, 8 - 0.5, 'resultat', label='quart de tour : atteint', size='s')
save(fig, '72-142')
