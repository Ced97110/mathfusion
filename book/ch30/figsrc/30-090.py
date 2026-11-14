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

fig, ax = canvas(74)
X = lambda x: 8 + x / PI * 72
Y = lambda y: 42 + y * 5.5
arrow(ax, (4, Y(0)), (86, Y(0)), 'fixe', lw=0.6)
dashv(ax, X(PI/2), Y(-4.3), Y(4.3))
curve(ax, np.cos, 0, PI, X, Y, 'fixe', ymax=2, lw=1.1)
curve(ax, sec, 0, PI, X, Y, 'sujet', ymax=3.8, lw=1.3)
disc(ax, X(PI/2), Y(0), 1.6, 'resultat')
text(ax, X(PI/2) + 3, Y(0) + 4, r'$f=0$ en $\pi/2$', 'resultat', 's', ha='left')
text(ax, X(PI/2), 69, r'asymptote de $1/f$', 'fixe', 's')
line(ax, [(6, 11.5), (14, 11.5)], 'fixe', lw=1.1); text(ax, 16, 11.5, r'$f=\cos x$', 'fixe', 's', ha='left')
line(ax, [(48, 11.5), (56, 11.5)], 'sujet', lw=1.3); text(ax, 58, 11.5, r'$1/f=\sec x$', 'sujet', 's', ha='left')
text(ax, 44, 5, r'$f(x)=0$ : $1\div0$ impossible', 'encre', 's')
save(fig, '30-090')
