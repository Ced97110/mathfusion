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
X = lambda x: 8 + x / PI * 72
Y = lambda y: 46 + y * 5.2
arrow(ax, (4, Y(0)), (84, Y(0)), 'fixe', lw=0.8)
dashv(ax, X(PI/2), Y(-5.4), Y(5.4))
curve(ax, sec, 0, PI, X, Y, 'sujet', ymax=5, lw=1.3)
text(ax, X(PI/2), 80, r'asymptote $x=\pi/2$', 'fixe', 's')
text(ax, 24, 66, r'$\sec x$', 'sujet', 'm')
text(ax, 44, 11, r'$\cos x=0$, numérateur $1\neq0$', 'encre', 's')
text(ax, 44, 6.8, r'$89{,}9°$ : $\cos x\approx0{,}0017453$', 'encre', 's')
text(ax, 44, 2.6, r'$\sec x\approx573$', 'sujet', 's')
save(fig, '30-081')
