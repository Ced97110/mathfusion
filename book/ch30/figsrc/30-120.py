import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(64)
X = lambda v: 10 + v * 11
Y = lambda v: 36 + 12 * v
B = math.pi / 4
numberline(ax, X(0), X(6), 36, 0, 6, labels=False, arrow_right=False)
curve(ax, lambda t: math.sin(B * (t - 2)), 0, 6, X, Y, 'sujet')
text(ax, X(0), 31.5, '0', 'fixe', 's'); text(ax, X(2), 31.5, '2', 'resultat', 's')
disc(ax, X(2), Y(0), 1.3, 'resultat')
text(ax, X(2) - 3, 41, 'angle 0', 'resultat', 's', ha='right')
arrow(ax, (X(0), 52), (X(2), 52), 'varie')
text(ax, X(1), 56, r'$C=2$', 'varie', 'm')
text(ax, 70, 52, r'$\sin(B(x-C))$', 'sujet', 's')
box(ax, 8, 3, 72, 9, 'resultat', label=r'$B(x-C)=0$ quand $x=C$')
save(fig, '30-120')
