import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(45)
y = 22
f = numberline(ax, 8, 70, y, 0, 40, step=5, arrow_right=False)
for v in (10, 35):
    disc(ax, f(v), y, 1.7, 'varie')
    text(ax, f(v), y + 5, 'permis', 'varie', 's')
disc(ax, f(25), y, 2.2, 'resultat')
text(ax, f(25), y + 6, r'$x = 25$', 'resultat', 'm', weight='bold')
disc(ax, f(30), y, 1.7, 'limite')
text(ax, f(30), y - 9, 'refusé', 'limite', 's')
save(fig, '12-003')
