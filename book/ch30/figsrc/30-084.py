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
f = numberline(ax, 8, 80, 57, -3, 3, 1, labels=False, arrow_right=False)
box(ax, f(-1), 52, f(1) - f(-1), 11, 'limite')
text(ax, f(0), 60.3, 'aucune valeur', 'limite', 's')
line(ax, [(f(-3), 57), (f(-1), 57)], 'resultat', lw=2.4); line(ax, [(f(1), 57), (f(3), 57)], 'resultat', lw=2.4)
disc(ax, f(0.5), 56, 1.2, 'limite')
text(ax, 4, 70, r'valeurs de $\sec x$', 'sujet', 'm', ha='left')
for v, s in ((-1, '−1'), (1, '1'), (0.5, '0,5')):
    text(ax, f(v) + (1.5 if v == 1 else -1.5 if v == 0.5 else 0), 48.5, s, 'limite' if v == 0.5 else 'fixe', 's')
g = numberline(ax, 8, 80, 22, -3, 3, 1, labels=False, arrow_right=False)
box(ax, g(-1), 17, g(1) - g(-1), 10, 'resultat')
text(ax, g(0), 24.3, 'entre −1 et 1', 'resultat', 's')
disc(ax, g(2), 22, 1.7, 'limite')
text(ax, 4, 35, r'valeurs de $\cos x$', 'sujet', 'm', ha='left')
for v, s in ((-1, '−1'), (1, '1'), (2, '2')):
    text(ax, g(v), 14, s, 'limite' if v == 2 else 'fixe', 's')
text(ax, g(2), 9, r'$\cos x=2$ : impossible', 'limite', 's')
arrow(ax, (f(0.5) + 0.6, 53), (g(2) - 0.4, 24.4), 'limite')
text(ax, 68, 40, r'$1\div0{,}5=2$', 'limite', 's', ha='left')
save(fig, '30-084')
