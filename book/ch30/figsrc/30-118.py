import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(80)
X = lambda v: 16 + v * 7.5
Y = lambda v: 30 + 1.1 * v
line(ax, [(14, Y(0)), (64, Y(0))], 'fixe', lw=0.5)
curve(ax, lambda t: 20 * math.sin(t), 0, 2 * math.pi, X, Y, 'fixe')
curve(ax, lambda t: 22 + 20 * math.sin(t), 0, 2 * math.pi, X, Y, 'sujet')
for v, s in ((42, r'$D+|A|=42$'), (2, r'$D-|A|=2$')):
    line(ax, [(14, Y(v)), (64, Y(v))], 'resultat', lw=0.8, dash=True)
    text(ax, 66, Y(v), s, 'resultat', 's', ha='left')
arrow(ax, (8, Y(0)), (8, Y(22)), 'varie')
text(ax, 8, Y(22) + 3.5, r'$D=22$', 'varie', 's')
text(ax, 51, 3.5, 'sans D', 'fixe', 's')
text(ax, 42, 68, 'avec D', 'sujet', 's')
save(fig, '30-118')
