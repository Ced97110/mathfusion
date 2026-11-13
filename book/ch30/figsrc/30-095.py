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

fig, ax = canvas(88)
text(ax, 44, 84, r'$y=A\sin(B(x-C))+D$', 'encre', 'l')
vals = [(r'départ : $x=\pi/2$', 'sujet'), (r'$\pi/4$', 'fixe'), (r'$\pi/2$', 'fixe'), ('1', 'fixe'), ('2', 'fixe'), (r'arrivée : $y=3$', 'resultat')]
acts = [r'retirer $C=\pi/4$', r'multiplier par $B=2$', r'sinus : $\sin(\pi/2)=1$', r'multiplier par $A=2$', r'ajouter $D=1$']
for i, (v, role) in enumerate(vals):
    yc = 72 - 13 * i
    box(ax, 12, yc - 3.5, 36, 7, role, label=v)
    if i < 5:
        arrow(ax, (30, yc - 4), (30, yc - 9.5), 'varie')
        text(ax, 54, yc - 6.75, acts[i], 'varie', 'm', ha='left')
save(fig, '30-095')
