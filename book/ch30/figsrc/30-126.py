import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(60)
X = lambda v: 10 + v * 10
Y = lambda v: 22 + 9 * v
line(ax, [(8, 22), (78, 22)], 'fixe', lw=0.5)
curve(ax, lambda t: math.sin(t), 0, 2 * math.pi, X, Y, 'fixe', lw=1.0)
A, B, C, D = 2, 2, math.pi / 4, 1
curve(ax, lambda t: D + A * math.sin(B * (t - C)), C, C + 2 * math.pi / B, X, Y, 'sujet')
for u, v in ((0, 0), (math.pi / 2, 1), (math.pi, 0), (3 * math.pi / 2, -1), (2 * math.pi, 0)):
    disc(ax, X(u), Y(v), 0.9, 'fixe')
    disc(ax, X(C + u / B), Y(D + A * v), 1.2, 'sujet')
arrow(ax, (X(math.pi / 2), Y(1) + 1.5), (X(math.pi / 2), Y(3) - 1.8), 'varie')
text(ax, X(math.pi / 2), Y(3) + 3.5, r'$(\pi/2\ ;\ 3)$', 'sujet', 's')
text(ax, 57, 9, r'$\sin x$', 'fixe', 's')
text(ax, 41, 6.5, 'transformée', 'sujet', 's')
text(ax, 69, 51, r'$x=C+u/B$', 'sujet', 'm'); text(ax, 69, 45, r'$y=D+Av$', 'sujet', 'm')
text(ax, 69, 38, r'$A=2,\ B=2$', 'encre', 's'); text(ax, 69, 33, r'$C=\pi/4,\ D=1$', 'encre', 's')
save(fig, '30-126')
