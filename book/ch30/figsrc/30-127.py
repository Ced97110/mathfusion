import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(64)
X = lambda v: 10 + v * 11
Y = lambda v: 36 + 15 * v
line(ax, [(8, 36), (80, 36)], 'fixe', lw=0.6)
curve(ax, lambda t: math.sin(t), 0, 2 * math.pi, X, Y, 'sujet')
labs = ['0', '1,571', '3,142', '4,712', '6,283']
for i in range(5):
    u = i * math.pi / 2; v = math.sin(u); role = 'sujet' if i % 2 == 0 else 'varie'
    line(ax, [(X(u), 14), (X(u), Y(v))], 'fixe', lw=0.5, dash=True)
    disc(ax, X(u), Y(v), 1.5, role)
    text(ax, X(u), 10, labs[i], 'fixe', 's')
text(ax, X(math.pi / 2) + 14, 56, 'le plus haut', 'varie', 's')
text(ax, X(3 * math.pi / 2) - 8.6, 18, 'le plus bas', 'varie', 's')
text(ax, 63, 44, 'trois points sur l’axe', 'sujet', 's')
save(fig, '30-127')
