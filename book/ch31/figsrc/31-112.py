import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(64)
f = numberline(ax, 14, 62, 50, -2, 2, labels=False, arrow_right=False)
g = numberline(ax, 14, 62, 16, -2, 2, labels=False, arrow_right=False)
disc(ax, f(-1), 50, 1.3, 'limite'); disc(ax, f(1), 50, 1.3, 'limite'); disc(ax, f(1), 16, 1.6, 'resultat')
text(ax, f(-1), 55, '−1', 'limite', 'm'); text(ax, f(1), 55, '1', 'limite', 'm'); text(ax, f(1), 10.5, '1', 'resultat', 'm')
arrow(ax, (f(-1) + 1, 47), (f(1) - 1.5, 19), 'varie'); arrow(ax, (f(1), 47), (f(1), 19), 'varie')
text(ax, f(1) + 3, 33, 'au carré, des deux côtés', 'varie', 's', ha='left')
text(ax, 44, 61, '−1 = 1 est faux', 'limite', 's')
text(ax, 44, 4, '(−1)² = 1² donne 1 = 1, vrai', 'resultat', 's')
save(fig, '31-112')
