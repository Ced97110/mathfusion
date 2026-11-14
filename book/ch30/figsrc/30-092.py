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
names = ['sin', 'cos', 'tan', 'sec', 'cot', 'cosec']
x0, L = 24, 58
pos = lambda t: x0 + t * L / 2
for k, s in enumerate(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']):
    dashv(ax, pos(k / 2), 6, 68); text(ax, pos(k / 2), 71, s, 'fixe', 's')
for i, n in enumerate(names):
    yc = 62 - 9 * i
    text(ax, 20, yc, n, 'encre', 'm', ha='right')
    line(ax, [(x0, yc), (x0 + L, yc)], 'fixe', lw=0.9)
    if i < 2: text(ax, 44, yc + 3.2, 'aucune', 'fixe', 's'); continue
    role, ts = ('sujet', (0.5, 1.5)) if i in (2, 3) else ('autre', (0, 1, 2))
    for t in ts: line(ax, [(pos(t), yc - 3), (pos(t), yc + 3)], role, lw=1.8)
save(fig, '30-092')
