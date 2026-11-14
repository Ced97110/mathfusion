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

fig, ax = canvas(62)
X = lambda x: 8 + x / (2*PI) * 72
Y = lambda y: 38 + y * 5.5
arrow(ax, (4, Y(0)), (86, Y(0)), 'fixe', lw=0.8)
for a in (PI/2, 3*PI/2): dashv(ax, X(a), Y(-3.5), Y(3.5))
curve(ax, sec, 0, 2*PI, X, Y, 'sujet', ymax=3.3, lw=1.3)
line(ax, [(X(0), Y(1)), (X(2*PI), Y(1))], 'resultat', lw=0.7, dash=True)
disc(ax, X(0), Y(1), 1.5, 'resultat'); disc(ax, X(2*PI), Y(1), 1.5, 'resultat'); disc(ax, X(PI), Y(-1), 1.5, 'limite')
text(ax, X(PI), Y(2.4), 'même valeur : 1', 'resultat', 's')
text(ax, X(PI), Y(-1) - 4.6, r'$\pi$ : $-1\neq1$', 'limite', 's')
for a, s in ((0, r'$x=0$'), (PI, r'$x=\pi$'), (2*PI, r'$x=2\pi$')):
    text(ax, X(a), 21, s, 'fixe', 's')
brace(ax, X(0), X(2*PI), 16, 'varie', label=r'période $2\pi$')
save(fig, '30-086')
