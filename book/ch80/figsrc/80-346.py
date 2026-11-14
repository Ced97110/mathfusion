import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
c, g = 7, 1.3
text(ax, 38, 69, "parties d'un ensemble de $n$", 'encre', 'm')
for row, (n, k) in enumerate([(1, 2), (2, 4), (3, 8)]):
    y = 52 - 15 * row
    for i in range(k):
        box(ax, 4 + (c + g) * i, y, c, c, 'sujet', r=0.5)
    text(ax, 72, y + c / 2, f'n = {n} : {k}', 'sujet', 's', ha='left')
for i in range(6):
    box(ax, 4 + (c + g) * i, 5, c, c, 'limite', fill=False, dash=True, r=0.5)
text(ax, 72, 8.5, 'aucun n', 'limite', 's', ha='left')
text(ax, 72, 4.5, 'donne 6', 'limite', 's', ha='left')
save(fig, '80-346')
