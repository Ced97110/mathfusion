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
rows = [(66, 'tan', r'$\sin x$', r'$\cos x$', 'sujet'), (50, 'sec', r'$1$', r'$\cos x$', 'sujet'),
        (30, 'cot', r'$\cos x$', r'$\sin x$', 'autre'), (14, 'cosec', r'$1$', r'$\sin x$', 'autre')]
for y, n, nu, de, role in rows:
    text(ax, 12, y, rf'$\mathrm{{{n}}}\,x=$', 'encre', 'm')
    text(ax, 32, y + 2.5, nu, 'encre', 'm')
    line(ax, [(24, y - 0.3), (40, y - 0.3)], 'encre', lw=0.8)
    box(ax, 24, y - 8, 16, 6.5, role, label=de, size='s')
box(ax, 56, 52, 30, 12, 'sujet', label=r'$\cos x=0$ (90°)')
box(ax, 56, 11, 30, 12, 'autre', label=r'$\sin x=0$ (0°)')
for y, ty, role in ((66, 60, 'sujet'), (50, 56, 'sujet'), (30, 18, 'autre'), (14, 16, 'autre')):
    arrow(ax, (40.6, y - 4.75), (55.4, ty), role, lw=0.9)
save(fig, '30-094')
