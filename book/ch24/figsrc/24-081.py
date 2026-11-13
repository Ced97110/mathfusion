import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
s, cx, y0 = 8.0, 22.0, 10.0
X = lambda v: cx + s * v
Y = lambda v: y0 + s * v
line(ax, [(X(-2.3), Y(0)), (X(2.4), Y(0))], 'fixe', lw=0.6)
n = 60
line(ax, [(X(-2.3 + 4.6 * i / n), Y((-2.3 + 4.6 * i / n) ** 2)) for i in range(n + 1)], 'sujet', lw=1.3)
line(ax, [(X(-1.8), Y(0.2)), (X(2.4), Y(4.4))], 'autre', lw=1.3)
for px, py in [(-1, 1), (2, 4)]:
    line(ax, [(X(px), Y(py)), (X(px), Y(0))], 'resultat', dash=True, lw=0.7)
    disc(ax, X(px), Y(py), 1.1, 'resultat')
text(ax, X(-1) - 1, Y(0) - 2.8, r'$-1$', 'resultat', 's')
text(ax, X(2), Y(0) - 2.8, r'$2$', 'resultat', 's')
bx, bw = 46, 40
box(ax, bx, 44, 19, 7, 'sujet', label=r'$y = x^2$', size='s')
box(ax, bx + 21, 44, 19, 7, 'autre', label=r'$y = x + 2$', size='s')
arrow(ax, (bx + 20, 43.5), (bx + 20, 38), 'varie')
text(ax, bx + 21, 40.8, 'on remplace y', 'varie', 's', ha='left')
box(ax, bx, 29, bw, 7, 'varie', label=r'$x^2 = x + 2$', size='s')
arrow(ax, (bx + 20, 28.5), (bx + 20, 23), 'varie')
box(ax, bx, 14, bw, 7, 'resultat', label=r'$x^2 - x - 2 = 0$', size='s')
save(fig, '24-081')
