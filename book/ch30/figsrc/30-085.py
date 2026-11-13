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

fig, ax = canvas(80)
box(ax, 2, 62, 44, 10, 'sujet', label=r'$|\cos x|\leq1$')
box(ax, 2, 38, 44, 10, 'varie', label=r'$|\sec x|=1/|\cos x|$')
box(ax, 2, 14, 44, 10, 'resultat', label=r'$|\sec x|\geq1$')
arrow(ax, (24, 61), (24, 49), 'fixe'); text(ax, 27, 55, 'on inverse', 'fixe', 's', ha='left')
arrow(ax, (24, 37), (24, 25), 'fixe'); text(ax, 27, 31, r'$1\div(\leq1)\geq1$', 'fixe', 's', ha='left')
x0, u = 54, 14
dashv(ax, x0 + u, 10, 74); text(ax, x0 + u, 77, '1', 'fixe', 'm')
box(ax, x0, 63.5, 0.5 * u, 6, 'sujet', r=0.3)
text(ax, x0, 74.2, r'$|\cos 60°|=0{,}5$', 'sujet', 's', ha='left')
box(ax, x0, 15.5, 2 * u, 6, 'resultat', r=0.3)
text(ax, x0, 26.5, r'$|\sec 60°|=2$', 'resultat', 's', ha='left')
save(fig, '30-085')
