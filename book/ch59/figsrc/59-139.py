import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 13, 60, 'on part de', 'fixe', 's')
text(ax, 44, 60, r'base de $K$', 'fixe', 's')
for y, lab in [(44, '3 points'), (30, '4 points'), (16, '100 points')]:
    text(ax, 13, y + 4, lab, 'varie', 's')
    arrow(ax, (26, y + 4), (35, y + 4), 'varie')
    for i in range(2):
        box(ax, 38 + i * 11, y - 1, 10, 10, 'sujet', r=0.6, label=r'$b_%d$' % (i + 1), size='s')
    text(ax, 75, y + 4, r'$m=2\leq n=2$', 'resultat', 's')
text(ax, 44, 5, r'$\mathbb{Z}^2$ a $n=2$ coordonnées', 'fixe', 's')
save(fig, '59-139')
