import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# f = y^2 - 3y + 2 cut in three pieces, each piece becomes one unknown
text(ax, 44, 70, r'$f=y^2-3y+2$', 'sujet', 'm', weight='bold')
xs = (16, 44, 72)
pieces = [r'$y^2$', r'$y$', r'$1$']
coefs = [r'$1\times$', r'$-3\times$', r'$2\times$']
names = [r'$Y_2$', r'$Y_1$', r'$Y_0$']
for x, p, c, n in zip(xs, pieces, coefs, names):
    box(ax, x - 9, 52, 18, 10, 'sujet', label=p, size='m')
    text(ax, x, 47, c, 'fixe', 's')
    arrow(ax, (x, 44), (x, 36), 'varie', lw=1.1)
    box(ax, x - 9, 25, 18, 10, 'resultat', label=n, size='m')
box(ax, 4, 6, 80, 11, 'resultat', label=r'$1\,Y_2-3\,Y_1+2\,Y_0$ : degré 1', size='s')
save(fig, '70-027')
