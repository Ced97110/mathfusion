import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 22, 66, 'un vecteur $x$', 'sujet', 's'); text(ax, 68, 66, 'une forme linéaire', 'autre', 's')
data = [(r'$x=(2,\,1)$', r'$y\mapsto2y_1+y_2$'), (r'$x=(1,\,0)$', r'$y\mapsto y_1$'), (r'$x=(0,\,1)$', r'$y\mapsto y_2$')]
for i, (a, b) in enumerate(data):
    y = 46 - 15 * i
    box(ax, 3, y, 38, 10, 'sujet', label=a)
    arrow(ax, (41, y + 5), (47, y + 5), 'varie', both=True)
    box(ax, 47, y, 39, 10, 'autre', label=b)
text(ax, 44, 8, r'chaque $f$ s’écrit $y\mapsto B(x,y)$', 'varie', 's')
save(fig, '71-079')
