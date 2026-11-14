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

fig, ax = canvas(62)
cx, cy, r = 24, 30, 18
circ(ax, cx, cy, r)
line(ax, [(cx - r - 2, cy), (cx + r + 2, cy)], 'fixe', lw=0.6)
arc(ax, cx, cy, 13, 0, 1.0, 'sujet', 1.4)
arc(ax, cx, cy, 21, 0, 1.0 + 2 * PI, 'varie', 1.2)
Px, Py = cx + r * np.cos(1.0), cy + r * np.sin(1.0)
line(ax, [(Px, Py), (52, Py)], 'fixe', lw=0.6, dash=True)
dot(ax, Px, Py, 'sujet'); dot(ax, 52, Py, 'resultat')
text(ax, 55, Py, r'$\sin=0{,}8415$', 'resultat', 's', ha='left')
text(ax, 50, 36, r'$x=1$', 'sujet', 's', ha='left')
text(ax, 50, 29, r'$x+2\pi=7{,}2832$', 'varie', 's', ha='left')
text(ax, 50, 22, 'même hauteur', 'resultat', 's', ha='left')
save(fig, '30-023')
