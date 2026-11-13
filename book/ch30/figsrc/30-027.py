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

fig, ax = canvas(66)
X0, Y0, SX, SY = 8, 36, 11.5, 15
X = lambda t: X0 + t * SX
Y = lambda v: Y0 + v * SY
arrow(ax, (X0 - 2, Y0), (84, Y0), 'fixe', lw=0.8)
curve(ax, np.sin, 0, 2 * PI, X, Y, 'sujet', 1.2, 400)
yt = Y(1) + 5
line(ax, [(X(PI / 2), Y(1)), (X(PI / 2), yt)], 'fixe', lw=0.5, dash=True)
line(ax, [(X(1.5 * PI), Y(-1)), (X(1.5 * PI), yt)], 'fixe', lw=0.5, dash=True)
arrow(ax, (X(PI / 2), yt), (X(1.5 * PI), yt), 'varie', lw=1.4)
text(ax, X(PI), yt + 3.2, r'$+\pi$', 'varie', 's')
dot(ax, X(PI / 2), Y(1), 'sujet', 1.3); dot(ax, X(1.5 * PI), Y(-1), 'limite', 1.3)
text(ax, X(PI / 2), Y(1) + 3.5, r'$\sin\frac{\pi}{2}=1$', 'sujet', 's', ha='right')
text(ax, X(1.5 * PI), Y(-1) - 3.5, r'$-1\neq1$ : échec', 'limite', 's')
for t in (0, PI):
    dot(ax, X(t), Y0, 'resultat', 1.3)
yb = Y0 - 6
arrow(ax, (X(0), yb), (X(PI), yb), 'varie', lw=1.4)
text(ax, X(PI / 2), yb - 3.2, r'$+\pi$', 'varie', 's')
text(ax, X(PI / 2), yb - 7.5, r'$\sin0=\sin\pi=0$', 'resultat', 's')
save(fig, '30-027')
