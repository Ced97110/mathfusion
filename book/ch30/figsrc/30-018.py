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

fig, ax = canvas(60)
cx, cy, r = 24, 30, 18
circ(ax, cx, cy, r)
line(ax, [(cx - r - 2, cy), (cx + r + 2, cy)], 'fixe', lw=0.6)
arc(ax, cx, cy, r, 0, PI / 2, 'varie', 1.6)
line(ax, [(cx, cy), (cx, cy + r)], 'resultat', lw=1.8)
line(ax, [(cx, cy + r), (56, cy + r)], 'fixe', lw=0.6, dash=True)
dot(ax, cx + r, cy, 'fixe'); dot(ax, cx, cy + r, 'sujet'); dot(ax, 56, cy + r, 'resultat')
text(ax, cx + r + 3, cy - 3, '$A$', 'fixe', 's')
text(ax, cx + 3, cy + r + 3, '$P$', 'sujet', 's')
text(ax, cx - 1.5, cy + 9, 'hauteur 1', 'resultat', 's', ha='right')
text(ax, 38, cy + 12, r'$x=\pi/2\approx1{,}57$', 'varie', 's', ha='left')
text(ax, 59, cy + r, r'$\sin x=1$', 'resultat', 's', ha='left')
save(fig, '30-018')
