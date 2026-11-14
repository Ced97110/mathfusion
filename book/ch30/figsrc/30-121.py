import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(74)
X = lambda v: 30 + 14 * v
Y = lambda v: 56 + 10 * v
line(ax, [(14, 56), (78, 56)], 'fixe')
line(ax, [(30, Y(-4) - 2), (30, 60)], 'fixe')
curve(ax, lambda t: (t - 1) ** 2 - 4, -0.9, 3, X, Y, 'sujet')
for xv in (0, 1, 2):
    v = (xv - 1) ** 2 - 4; disc(ax, X(xv), Y(v), 1.2, 'resultat' if xv == 1 else 'varie')
line(ax, [(X(1), Y(-4)), (X(1), 54.5)], 'resultat', lw=0.6, dash=True)
text(ax, X(0) - 2, 52, '0', 'fixe', 's'); text(ax, X(1) + 2.5, 52, '1', 'resultat', 's')
arrow(ax, (X(0), 62), (X(1), 62), 'varie')
text(ax, X(0.5), 66, 'sommet : de 0 à 1', 'varie', 's')
text(ax, X(1), Y(-4) - 5, r'sommet : $x-1=0$ en $x=1$', 'resultat', 's')
text(ax, 68, 3.5, r'$y=(x-1)^2-4$', 'sujet', 'm')
save(fig, '30-121')
