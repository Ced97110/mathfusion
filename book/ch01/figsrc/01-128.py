import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
f = numberline(ax, 8, 73, 14, 0, 5, 1, labels=False)
text(ax, 66, 48, '> : plus grand que', 'fixe', 's')
for k in range(6):
    box(ax, f(k) - 5.5, 20, 11, 7, 'limite', label=f'{k} > {k+1}', size='s')
text(ax, 40, 7, 'fausse pour 0, 1, 2, 3 …', 'fixe', 's')
for k in range(5):
    arrow(ax, (f(k), 28), (f(k+1), 28), 'varie', curve=-0.5)
text(ax, 40, 38, 'passage vrai', 'varie', 's')
text(ax, 16, 48, 'départ : faux', 'limite', 's')
arrow(ax, (12, 45.5), (8, 28.5), 'limite')
save(fig, '01-128')
