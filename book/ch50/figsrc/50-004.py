import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
exc = {5, 7, 8, 9, 10, 11}
text(ax, 44, 35, 'tailles possibles pour 12 éléments', 'encre', 'm')
for i in range(12):
    n = i + 1
    if n in exc: box(ax, 2 + 7 * i, 18, 6.6, 11, 'limite', label=str(n), size='s', r=0.4)
    else: box(ax, 2 + 7 * i, 18, 6.6, 11, 'fixe', label=str(n), size='s', r=0.4, dash=True)
box(ax, 4, 5, 6, 6, 'limite', r=0.4)
text(ax, 13, 8, 'exclue', 'limite', 's', ha='left')
box(ax, 36, 5, 6, 6, 'fixe', r=0.4, dash=True)
text(ax, 45, 8, 'permise, pas garantie', 'fixe', 's', ha='left')
save(fig, '50-004')
