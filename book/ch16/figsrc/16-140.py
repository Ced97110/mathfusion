import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
f = numberline(ax, 8, 78, 6, -6, 8, 1, every=2, arrow_right=False)
yA, yB, yC = 34, 56, 14
def two(y, a, b):
    disc(ax, f(a), y, 1.5, 'sujet'); disc(ax, f(b), y, 1.5, 'autre')
two(yA, 3, 5); two(yB, 5, 7); two(yC, -3, -5)
arrow(ax, (f(3), yA + 2), (f(5), yB - 2), 'varie'); arrow(ax, (f(5), yA + 2), (f(7), yB - 2), 'varie')
arrow(ax, (f(3), yA - 2), (f(-3), yC + 2), 'varie'); arrow(ax, (f(5), yA - 2), (f(-5), yC + 2), 'varie')
text(ax, 14, 46, '+ 2', 'varie', 'm'); text(ax, 14, 24, '× (−1)', 'varie', 'm')
text(ax, 62, yB + 8, '5 < 7 : même sens', 'resultat', 's'); text(ax, 62, yA + 8, '3 < 5', 'fixe', 's')
text(ax, 60, yC + 8, '−3 > −5 : sens inverse', 'limite', 's')
save(fig, '16-140')
