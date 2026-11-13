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
X = lambda x: 8 + (x + PI/2) / (1.5*PI) * 72
Y = lambda y: 16 + y * 8
arrow(ax, (4, Y(0)), (86, Y(0)), 'fixe', lw=0.8)
for a in (-PI/2, PI/2): dashv(ax, X(a), Y(0), Y(4.5))
for a in (0, PI): dashv(ax, X(a), Y(0), Y(4.5), 'sujet')
curve(ax, sec, -PI/2, PI, X, Y, 'fixe', ymax=4.2, ymin=0, lw=1.3)
curve(ax, csc, 0, PI, X, Y, 'sujet', ymax=4.2, ymin=0, lw=1.3)
disc(ax, X(0), Y(1), 1.4, 'fixe'); disc(ax, X(PI/2), Y(1), 1.4, 'sujet')
arrow(ax, (X(0) + 2, Y(1)), (X(PI/2) - 2, Y(1)), 'varie')
text(ax, X(PI/4), 20.5, r'$+\pi/2$ vers la droite', 'varie', 's')
text(ax, X(-1.0), Y(3.6), r'$\sec x$', 'fixe', 's')
text(ax, X(2.0), Y(3.6), r'$\mathrm{cosec}\,x$', 'sujet', 's')
for a, s in ((-PI/2, r'$-\pi/2$'), (0, '0'), (PI/2, r'$\pi/2$'), (PI, r'$\pi$')):
    text(ax, X(a), 11, s, 'fixe', 's')
text(ax, 44, 4.5, r'$\mathrm{cosec}\,x=\sec(x-\pi/2)$', 'sujet', 'm')
save(fig, '30-088')
