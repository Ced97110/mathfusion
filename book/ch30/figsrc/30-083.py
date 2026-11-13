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

fig, ax = canvas(66)
X = lambda x: 8 + (x + PI/2) / (2*PI) * 72
Y = lambda y: 33 + y * 5.5
arrow(ax, (4, Y(0)), (84, Y(0)), 'fixe', lw=0.8)
for a, s in ((-PI/2, r'$-\pi/2$'), (PI/2, r'$\pi/2$'), (3*PI/2, r'$3\pi/2$')):
    dashv(ax, X(a), Y(-4.6), Y(4.6)); text(ax, X(a), 62, s, 'fixe', 's')
curve(ax, sec, -PI/2, PI/2, X, Y, 'sujet', ymax=4.2, lw=1.3)
curve(ax, sec, PI/2, 3*PI/2, X, Y, 'autre', ymax=4.2, lw=1.3)
text(ax, X(0), Y(0.5), 'sommet 1', 'sujet', 's')
text(ax, X(PI), Y(-0.5), 'sommet −1', 'autre', 's')
text(ax, X(0), Y(2.7), 'ouvert en haut', 'sujet', 's')
text(ax, X(PI), Y(-2.7), 'ouvert en bas', 'autre', 's')
save(fig, '30-083')
