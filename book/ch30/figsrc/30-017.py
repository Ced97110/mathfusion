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
X0, Y0, SX, SY = 12, 32, 11.5, 14
X = lambda t: X0 + t * SX
Y = lambda v: Y0 + v * SY
arrow(ax, (3, Y0), (86, Y0), 'fixe', lw=0.8)
curve(ax, np.cos, -0.75, 6.2, X, Y, 'autre')
curve(ax, np.sin, 0, 6.2, X, Y, 'sujet')
ya = Y0 + SY + 5
for t in (0, PI / 2):
    line(ax, [(X(t), Y0), (X(t), ya)], 'fixe', lw=0.6, dash=True)
dot(ax, X(0), Y(1), 'autre'); dot(ax, X(PI / 2), Y(1), 'sujet')
arrow(ax, (X(PI / 2) - 0.5, ya), (X(0) + 0.5, ya), 'varie', lw=1.4)
text(ax, (X(0) + X(PI / 2)) / 2, ya - 3, r'$\pi/2$', 'varie', 's')
text(ax, X(0), ya + 3.5, '(0, 1)', 'autre', 's')
text(ax, X(PI / 2), ya + 3.5, r'$(\pi/2,\ 1)$', 'sujet', 's')
text(ax, X(PI), Y(-1) - 3.5, 'cosinus', 'autre', 's')
text(ax, X(1.5 * PI), Y(-1) - 3.5, 'sinus', 'sujet', 's')
save(fig, '30-017')
