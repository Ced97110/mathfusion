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

fig, ax = canvas(54)
f = numberline(ax, 6, 76, 20, -3, 3, 1)
for v, r in ((-0.5, 'sujet'), (-2, 'resultat'), (2, 'limite')):
    disc(ax, f(v), 20, 1.7, r)
text(ax, f(-0.5), 29, r'$\cos 120°=-0{,}5$', 'sujet', 's')
line(ax, [(f(-0.5), 27.4), (f(-0.5), 22)], 'sujet')
text(ax, f(-2), 38, r'$\sec=1/(-0{,}5)=-2$', 'resultat', 's')
line(ax, [(f(-2), 36.4), (f(-2), 22)], 'resultat')
text(ax, f(2), 29, r'$-1/\cos=2$', 'limite', 's')
line(ax, [(f(2), 27.4), (f(2), 22)], 'limite')
text(ax, f(-1.5), 48, '← négatif', 'fixe', 's')
text(ax, f(1.5), 48, 'positif →', 'fixe', 's')
save(fig, '30-082')
