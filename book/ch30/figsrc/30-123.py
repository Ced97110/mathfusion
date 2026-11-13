import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(64)
X = lambda v: 10 + v * 62 / math.pi
Y = lambda v: 36 + 12 * v
line(ax, [(X(0), 36), (X(math.pi), 36)], 'fixe')
curve(ax, lambda t: math.sin(2 * t - math.pi / 2), 0, math.pi, X, Y, 'sujet')
disc(ax, X(math.pi / 4), 36, 1.4, 'resultat'); disc(ax, X(math.pi / 2), 36, 1.4, 'limite')
text(ax, X(math.pi / 4) - 1, 31.5, r'$\pi/4$', 'resultat', 's', ha='right')
text(ax, X(math.pi / 2) + 1, 31.5, r'$\pi/2$', 'limite', 's', ha='left')
text(ax, X(math.pi / 4) - 2, 57, 'décalage', 'resultat', 's', ha='right')
arrow(ax, (X(math.pi / 4) - 2, 54), (X(math.pi / 4), 38.5), 'resultat', lw=0.8)
text(ax, X(math.pi / 2) + 2, 57, 'pas le décalage', 'limite', 's', ha='left')
arrow(ax, (X(math.pi / 2) + 2, 54), (X(math.pi / 2), 38.5), 'limite', lw=0.8)
text(ax, 70, 47, r'$\sin(2x-\pi/2)$', 'sujet', 's')
box(ax, 8, 3, 72, 10, 'resultat', label=r'décalage $=c/B=\pi/4$')
save(fig, '30-123')
