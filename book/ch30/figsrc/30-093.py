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
cx, cy, r = 26, 40, 16
line(ax, [(6, cy), (46, cy)], 'fixe', lw=0.6); line(ax, [(cx, 22), (cx, 58)], 'fixe', lw=0.6)
disc(ax, cx, cy, r, 'sujet', fill=False, lw=1.0)
c, s = math.cos(math.radians(30)), math.sin(math.radians(30))
line(ax, [(cx - r*c, cy - r*s), (cx + r*c, cy + r*s)], 'encre', lw=0.8, dash=True)
disc(ax, cx + r*c, cy + r*s, 1.6, 'sujet'); disc(ax, cx - r*c, cy - r*s, 1.6, 'varie')
text(ax, cx + r*c + 3, cy + r*s + 3, r'$P$', 'sujet', 'm'); text(ax, cx - r*c - 3, cy - r*s - 3, r"$P'$", 'varie', 'm')
for yb, role, d, sg in ((46, 'sujet', '30°', '+'), (14, 'varie', '210°', '−')):
    box(ax, 56, yb, 30, 24, role)
    text(ax, 71, yb + 20, d, role, 'm', weight='bold')
    text(ax, 71, yb + 15, f'cos {sg}, sin {sg}', role, 's')
    text(ax, 71, yb + 10, 'tan = 0,577', role, 's')
    text(ax, 71, yb + 5, 'cot = 1,732', role, 's')
text(ax, 71, 42, 'mêmes valeurs', 'resultat', 's')
save(fig, '30-093')
