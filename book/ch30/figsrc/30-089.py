import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
PI = np.pi
sec = lambda x: 1 / np.cos(x)
csc = lambda x: 1 / np.sin(x)
def curve(ax, f, xa, xb, X, Y, role='sujet', ymax=3.0, ymin=None, lw=1.1, n=900):
    xs = np.linspace(xa, xb, n); seg = []
    lo = -ymax if ymin is None else ymin
    with np.errstate(all='ignore'): ys = f(xs)
    for x, y in zip(xs, ys):
        if np.isfinite(y) and lo <= y <= ymax: seg.append((float(X(x)), float(Y(y))))
        else:
            if len(seg) > 1: line(ax, seg, role, lw)
            seg = []
    if len(seg) > 1: line(ax, seg, role, lw)
def dashv(ax, x, y0, y1, role='fixe'): line(ax, [(x, y0), (x, y1)], role, lw=0.7, dash=True)

fig, ax = canvas(76)
X = lambda x: 8 + x / (2*PI) * 72
Y = lambda y: 40 + y * 5.5
arrow(ax, (4, Y(0)), (86, Y(0)), 'fixe', lw=0.6)
for a, s in ((0, '0'), (PI, r'$\pi$'), (2*PI, r'$2\pi$')):
    dashv(ax, X(a), Y(-3.9), Y(3.9)); text(ax, X(a), 65, s, 'fixe', 's')
text(ax, 44, 71.5, r'asymptotes : $x=k\pi$', 'fixe', 'm')
curve(ax, csc, 0, 2*PI, X, Y, 'sujet', ymax=3.4, lw=1.3)
disc(ax, X(PI/2), Y(1), 1.5, 'resultat')
text(ax, X(PI/2), Y(1.9), r'$\pi/2$ : valeur 1', 'resultat', 's')
text(ax, X(PI/2), Y(2.9), r'$\mathrm{cosec}\,x$', 'sujet', 's')
text(ax, X(PI), 13, r'$\sin\pi=0$ : pas de valeur', 'fixe', 's')
save(fig, '30-089')
