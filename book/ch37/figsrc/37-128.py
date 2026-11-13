import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 10, 80, 20, 0, 10, labels=False, arrow_right=False)
for v, role in ((0, 'sujet'), (4, 'sujet'), (10, 'sujet')):
    disc(ax, f(v), 20, 1.1, role); text(ax, f(v), 15.5, f'{v}', 'sujet', 's')
for v in (2, 7, 5):
    line(ax, [(f(v), 20), (f(v), 44)], 'varie', lw=1.0)
    disc(ax, f(v), 20, 0.8, 'varie')
    text(ax, f(v), 47.5, f'{v}', 'varie', 's')
text(ax, 44, 52.5, 'milieux et médiatrices', 'varie', 's')
text(ax, 44, 7, 'parallèles : aucun point commun', 'limite', 'm')
save(fig, '37-128')
