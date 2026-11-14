import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
PI = np.pi
def curve(ax, f, a, b, X, Y, role='sujet', lw=1.2, n=240):
    t = np.linspace(a, b, n); ax.plot(X(t), Y(f(t)), color=COL[role], lw=lw, zorder=3, solid_capstyle='round')
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.4, head=True):
    t = np.linspace(a0, a1, 200); xs = cx + r * np.cos(t); ys = cy + r * np.sin(t)
    ax.plot(xs, ys, color=COL[role], lw=lw, zorder=3, solid_capstyle='round')
    if head: arrow(ax, (xs[-4], ys[-4]), (xs[-1], ys[-1]), role, lw=lw)
def circ(ax, cx, cy, r, role='fixe'):
    t = np.linspace(0, 2 * PI, 300); ax.plot(cx + r * np.cos(t), cy + r * np.sin(t), color=COL[role], lw=1.0, zorder=2)
def dot(ax, x, y, role, r=1.1):
    ax.add_patch(Circle((x, y), r, fc=COL[role], ec=COL[role], zorder=4))

fig, ax = canvas(72)
cx, cy, r = 26, 36, 18
circ(ax, cx, cy, r)
ax_x = 56
arrow(ax, (ax_x, cy - r - 4), (ax_x, cy + 1.2 * r + 5), 'fixe', lw=0.8)
for v in (-1, 0, 1):
    yy = cy + v * r
    line(ax, [(ax_x - 1.2, yy), (ax_x + 1.2, yy)], 'fixe', lw=0.8)
    text(ax, ax_x + 3, yy, f'{v}'.replace('-', '\u2212'), 'fixe', 's', ha='left')
for v in (1, -1):
    line(ax, [(cx, cy + v * r), (ax_x, cy + v * r)], 'resultat', lw=0.7, dash=True)
    dot(ax, cx, cy + v * r, 'resultat')
line(ax, [(cx - r - 3, cy + 1.2 * r), (ax_x, cy + 1.2 * r)], 'limite', lw=0.8, dash=True)
text(ax, cx - 4, cy + 1.2 * r + 3, '1,2 : hors du cercle', 'limite', 's')
line(ax, [(cx, cy), (cx, cy + r)], 'sujet', lw=1.6)
text(ax, cx - 1.8, cy + r / 2, 'rayon 1', 'sujet', 's', ha='right')
arrow(ax, (66, cy - r), (66, cy + r), 'fixe', lw=1.0, both=True)
text(ax, 70, cy, 'écart 2', 'fixe', 's', rot=90)
arrow(ax, (77, cy), (77, cy + r), 'varie', lw=1.2)
text(ax, 81, cy + r / 2, 'moitié : 1', 'varie', 's', rot=90)
save(fig, '30-025')
