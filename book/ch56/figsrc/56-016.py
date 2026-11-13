import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
f = numberline(ax, 8, 68, 14, 0, 9, step=1)
box(ax, f(2), 14.5, f(3) - f(2), 33.5, 'limite', r=0.3)
for v in (0, 1, 4, 9):
    disc(ax, f(v), 38, 1.3, 'sujet')
for v in (5, 6, 9):
    disc(ax, f(v), 26, 1.3, 'varie')
text(ax, 86, 43.5, 'b = 0 : a²', 'sujet', 's', ha='right')
text(ax, 86, 31.5, 'b ≠ 0 : a² + 5b² ≥ 5', 'varie', 's', ha='right')
text(ax, f(2.5), 53, '2 et 3 : aucune valeur', 'limite', 's')
save(fig, '56-016')
