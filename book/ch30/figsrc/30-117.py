import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(62)
X = lambda v: 10 + v * 10
Y = lambda v: 31 + 7 * v
line(ax, [(X(0), 31), (X(2 * math.pi), 31)], 'fixe', lw=0.5)
for v, s in ((3, r'$|A|=3$'), (-3, r'$-|A|=-3$')):
    line(ax, [(8, Y(v)), (74, Y(v))], 'resultat', lw=0.8, dash=True)
    text(ax, 75, Y(v), s, 'resultat', 's', ha='left')
curve(ax, lambda t: math.sin(t), 0, 2 * math.pi, X, Y, 'fixe')
curve(ax, lambda t: 3 * math.sin(t), 0, 2 * math.pi, X, Y, 'sujet')
text(ax, 26, 57, r'$3\,\sin x$', 'sujet', 'm')
text(ax, 60, 36.5, r'$\sin x$', 'fixe', 's')
save(fig, '30-117')
