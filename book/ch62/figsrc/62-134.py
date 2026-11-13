import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(88)
X = lambda x: 8 + (x + 2.4) * 16.1
Y = lambda y: 36 + y * 4.4
f = lambda x: (x - 1) ** 2 * (x + 2)
fp = lambda x: 3 * x ** 2 - 3
# repère
arrow(ax, (5, Y(0)), (86, Y(0)), 'fixe', lw=0.9)
for v in (-2, 1):
    ax.plot([X(v), X(v)], [Y(0) - 1, Y(0) + 1], color=COL['fixe'], lw=0.8, zorder=1.5)
    text(ax, X(v) + (3 if v < 0 else 0), Y(0) - 3.4, f'{v}'.replace('-', '−'), 'fixe', 's')
# courbes (coupées à la hauteur 10)
xs = np.linspace(-2.4, 2.2, 400)
pf = [(X(x), Y(f(x))) for x in xs if -5 <= f(x) <= 10]
pp = [(X(x), Y(fp(x))) for x in xs if -5 <= fp(x) <= 10]
line(ax, pf, 'sujet', lw=1.3)
line(ax, pp, 'varie', lw=1.3)
text(ax, 84.5, Y(f(2.2)) - 1, r'$f$', 'sujet', 'l')
text(ax, 84.5, Y(10) - 3, r"$f\,'$", 'varie', 'l', weight='bold')
# racine double en 1 : f touche l'axe, f' est sur l'axe
disc(ax, X(1), Y(0), 1.6, 'resultat')
text(ax, 73, Y(0) - 8.5, 'racine double', 'resultat', 's')
text(ax, 73, Y(0) - 12, 'f touche l’axe', 'sujet', 's')
# racine simple en -2 : f traverse, f' vaut 9
disc(ax, X(-2), Y(0), 1.6, 'sujet')
text(ax, 25, Y(0) - 8.5, 'racine simple', 'sujet', 's')
text(ax, 25, Y(0) - 12, 'f traverse l’axe', 'sujet', 's')
disc(ax, X(-2), Y(fp(-2)), 1.6, 'varie')
text(ax, X(-2) + 11, Y(fp(-2)), r"$f\,'(-2)=9$", 'varie', 's')
save(fig, '62-134')
