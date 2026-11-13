import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
f = numberline(ax, 6, 76, 8, -16, 8, 4, arrow_right=False)
yA, yC = 52, 26
disc(ax, f(2), yA, 1.5, 'sujet'); disc(ax, f(7), yA, 1.5, 'autre')
disc(ax, f(-4), yC, 1.5, 'sujet'); disc(ax, f(-14), yC, 1.5, 'autre')
arrow(ax, (f(2), yA - 2), (f(-4), yC + 2), 'varie'); arrow(ax, (f(7), yA - 2), (f(-14), yC + 2), 'varie')
text(ax, 44, yA + 8, '2 < 7 : vrai', 'resultat', 'm'); text(ax, 14, 39, '× (−2)', 'varie', 'm')
text(ax, 44, 15, '−4 < −14 : faux', 'limite', 'm')
save(fig, '16-145')
