import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 8, 66, 16, -2, 5, arrow_right=True)
text(ax, 84, 22, r'$x$', 'sujet', 'xl')
for v, lab, cx in [(2.1, r'$x$ vaut 2,1', 18), (3, r'$x$ vaut 3', 56)]:
    disc(ax, f(v), 16, 1.6, 'varie')
    box(ax, cx - 14, 36, 28, 8, 'varie', label=lab, size='s')
    arrow(ax, (cx, 35.5), (f(v), 18.2), 'varie')
text(ax, 44, 54, r'les nombres sont les valeurs de $x$', 'sujet', 's')
save(fig, '17-013')
