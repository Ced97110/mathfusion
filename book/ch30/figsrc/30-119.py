import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(54)
X = lambda v: 8 + (v + 1) * 8.5
Y = lambda v: 28 + 13 * v
numberline(ax, X(-1), X(7), 28, -1, 7, labels=False, arrow_right=False)
text(ax, X(0), 24.4, '0', 'fixe', 's'); text(ax, X(2), 24.4, '2', 'resultat', 's')
curve(ax, lambda t: math.sin(t - 2), -1, 7, X, Y, 'sujet')
for v, lab, dx in ((0, r'$-0{,}909$', -2), (2, None, 0), (3, r'$0{,}841$', 0)):
    y = math.sin(v - 2); disc(ax, X(v), Y(y), 1.2, 'resultat' if v == 2 else 'varie')
text(ax, X(0) - 2.5, Y(math.sin(-2)), r'$-0{,}909$', 'varie', 's', ha='right')
text(ax, X(3) - 1.5, Y(math.sin(1)) + 3.5, r'$0{,}841$', 'varie', 's', ha='right')
arrow(ax, (X(0), 36), (X(2), 36), 'varie')
text(ax, X(0.6), 40, 'départ : x = 2', 'varie', 's')
text(ax, 70, 46, r'$\sin(x-2)$', 'sujet', 'm')
save(fig, '30-119')
