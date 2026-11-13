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

fig, ax = canvas(64)
X0, SX = 16, 8.0
Y = lambda m: 10 + (m - 2)
for m in (2, 22, 42):
    line(ax, [(X0 - 1, Y(m)), (62, Y(m))], 'fixe', lw=0.5, dash=True)
    text(ax, 2.5, Y(m), f'{m} m', 'fixe', 's', ha='left')
t = np.linspace(0, 1.5 * 2 * PI, 300)
ax.plot(X0 + t * 4.0 * 0.82 * 1.0, Y(22 + 20 * np.sin(t)), color=COL['sujet'], lw=1.5, zorder=3)
arrow(ax, (67, Y(2)), (67, Y(42)), 'fixe', lw=1.0, both=True)
text(ax, 71.5, Y(22), 'écart 40 m', 'fixe', 's', rot=90)
arrow(ax, (78, Y(22)), (78, Y(42)), 'resultat', lw=1.4)
text(ax, 82.5, Y(32), 'moitié : 20 m', 'resultat', 's', rot=90)
text(ax, 40, 60, 'cabine de la roue', 'sujet', 's')
save(fig, '30-029')
