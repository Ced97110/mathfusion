import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(56)
X = lambda v: 8 + v * 10
Y = lambda v: 26 + 12 * v
f = numberline(ax, 8, 78, 7, 0, 7, arrow_right=False)
curve(ax, lambda t: math.sin(t), 0, 7, X, Y, 'fixe')
curve(ax, lambda t: math.sin(t - 2), 0, 7, X, Y, 'sujet')
for v, role in ((math.pi / 2, 'fixe'), (math.pi / 2 + 2, 'sujet')):
    line(ax, [(X(v), 7), (X(v), Y(1))], role, lw=0.6, dash=True)
    disc(ax, X(v), Y(1), 1.1, role)
text(ax, X(math.pi / 2) - 1, 41, '1,571', 'fixe', 's', ha='right')
text(ax, X(math.pi / 2 + 2), 41.5, '3,571', 'sujet', 's')
arrow(ax, (X(math.pi / 2) + 1, 45), (X(math.pi / 2 + 2) - 1, 45), 'varie')
text(ax, X(math.pi / 2 + 1), 49, r'$+\,2$', 'varie', 'm')
text(ax, 13, 38, r'$\sin x$', 'fixe', 's')
text(ax, 66, 40, r'$\sin(x-2)$', 'sujet', 's')
save(fig, '30-114')
