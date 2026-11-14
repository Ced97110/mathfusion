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
names = ['sin', 'cos', 'sec', 'cosec', 'tan', 'cot']
per = [2, 2, 2, 2, 1, 1]
x0, pi_mm = 24, 18
for i, (n, p) in enumerate(zip(names, per)):
    yc = 68 - 10 * i
    text(ax, 20, yc, n, 'encre', 'm', ha='right')
    role = 'sujet' if p == 2 else 'varie'
    box(ax, x0, yc - 3, p * pi_mm, 6, role, r=0.4)
    text(ax, x0 + p * pi_mm + 2, yc, r'$2\pi$' if p == 2 else r'$\pi$', role, 'm', ha='left')
for k in (1, 2):
    dashv(ax, x0 + k * pi_mm, 8, 74)
save(fig, '30-091')
