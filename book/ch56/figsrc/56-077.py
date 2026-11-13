import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(82)
nodes = {'1': (44, 20, 'fixe'), '2': (22, 42, 'fixe'), '3': (66, 42, 'fixe'), '6': (44, 64, 'resultat')}
r = 5.8
for k, (x, y, role) in nodes.items():
    disc(ax, x, y, r, role, label=k, size='l')
def link(a, b):
    (xa, ya, _), (xb, yb, _) = nodes[a], nodes[b]
    d = math.hypot(xb - xa, yb - ya); ux, uy = (xb - xa) / d, (yb - ya) / d
    arrow(ax, (xa + ux * (r + 0.5), ya + uy * (r + 0.5)), (xb - ux * (r + 0.5), yb - uy * (r + 0.5)), 'varie')
for a, b in [('1', '2'), ('1', '3'), ('2', '6'), ('3', '6')]:
    link(a, b)
text(ax, 44, 77, 'diviseurs communs de 12 et 18', 'encre', 's')
text(ax, 86, 64, '$-6$ convient aussi', 'resultat', 's', ha='right')
text(ax, 3, 20, 'flèche : divise', 'varie', 's', ha='left')
text(ax, 44, 6, 'tout diviseur commun divise 6', 'resultat', 's')
save(fig, '56-077')
