import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
y = 24
f = numberline(ax, 8, 68, y, -3, 3)
for a, b, c in ((0, 1, -0.5), (1, 2, -0.5), (0, -1, 0.5), (-1, -2, 0.5)):
    arrow(ax, (f(a), y + 2), (f(b), y + 2), 'varie', curve=c)
disc(ax, f(2), y, 1.7, 'resultat'); disc(ax, f(-2), y, 1.7, 'resultat')
disc(ax, f(0.5), y, 1.7, 'autre')
text(ax, f(0.5), y - 9.5, r'$1/2$ : aucun arc n’arrive', 'autre', 's')
text(ax, f(1), y + 9, '2 fois à droite', 'varie', 's')
text(ax, f(-1), y + 9, '2 fois à gauche', 'varie', 's')
text(ax, f(2), y + 4.5, '2', 'resultat', 's')
text(ax, f(-2), y + 4.5, '−2', 'resultat', 's')
save(fig, '12-011')
