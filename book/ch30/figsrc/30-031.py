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
X0, Y0, SX, SY = 24.5, 28, 6.2, 14
X = lambda t: X0 + t * SX
Y = lambda v: Y0 + v * SY
arrow(ax, (3, Y0), (86, Y0), 'fixe', lw=0.8)
curve(ax, np.sin, -PI, 3 * PI, X, Y, 'sujet', 1.2, 500)
for k, lab in zip(range(-1, 4), [r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$']):
    dot(ax, X(k * PI), Y0, 'resultat', 1.4)
    text(ax, X(k * PI), Y0 - 4.5, lab, 'resultat', 's')
dot(ax, X(PI / 2), Y(1), 'limite', 1.4)
text(ax, X(PI / 2), Y(1) + 3.5, r'$\pi/2$ : sin = 1', 'limite', 's')
text(ax, X(2.5 * PI), Y(-1) - 3.5, 'zéros : sin = 0', 'resultat', 's')
text(ax, 44, 57, r'$x=k\pi$, $k$ entier', 'sujet', 'm')
save(fig, '30-031')
