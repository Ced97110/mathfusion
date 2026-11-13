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

fig, ax = canvas(84)
X = lambda x: 8 + x / (2*PI) * 72
Y = lambda y: 56 + y * 5.5
arrow(ax, (4, Y(0)), (86, Y(0)), 'fixe', lw=0.6)
for a, s in ((0, '0'), (PI, r'$\pi$'), (2*PI, r'$2\pi$')):
    dashv(ax, X(a), Y(-3.8), Y(3.8)); text(ax, X(a), 80, s, 'fixe', 's')
curve(ax, np.sin, 0, 2*PI, X, Y, 'fixe', ymax=2, lw=0.9)
curve(ax, csc, 0, 2*PI, X, Y, 'sujet', ymax=3.4, lw=1.3)
text(ax, X(PI/2), Y(2.4), r'$\mathrm{cosec}\,x$', 'sujet', 's')
text(ax, X(PI/2), Y(0.45), r'$\sin x$', 'fixe', 's')
box(ax, 6, 8, 32, 11, 'varie', label=r'$1°$ : $\approx57{,}30$', size='s')
box(ax, 50, 8, 32, 11, 'varie', label=r'$0{,}5°$ : $\approx114{,}6$', size='s')
arrow(ax, (39, 13.5), (49, 13.5), 'varie')
text(ax, 44, 24, 'angle plus petit', 'varie', 's')
save(fig, '30-087')
