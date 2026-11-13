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

fig, ax = canvas(80)
X0, Y0, SX, SY = 8, 40, 8.0, 14
X = lambda t: X0 + t * SX
Y = lambda v: Y0 + v * SY
arrow(ax, (X0 - 2, Y0), (87, Y0), 'fixe', lw=0.8)
for v in (1, -1):
    line(ax, [(X0 - 1, Y(v)), (X(3 * PI), Y(v))], 'fixe', lw=0.5, dash=True)
curve(ax, np.cos, 0, 3 * PI, X, Y, 'sujet', 1.2, 400)
text(ax, 4, Y(1), '1', 'fixe', 's'); text(ax, 4, Y(-1), '\u22121', 'fixe', 's')
for k, lab in enumerate(['0', r'$\pi$', r'$2\pi$', r'$3\pi$']):
    text(ax, X(k * PI), Y0 + 3.2, lab, 'fixe', 's')
    dot(ax, X(k * PI), Y((-1) ** k), 'sujet', 1.3)
yt = Y(1) + 6
arrow(ax, (X(0), yt), (X(2 * PI), yt), 'varie', lw=1.4)
text(ax, X(PI), yt + 3.2, r'$+2\pi$', 'varie', 's')
yb = Y(-1) - 6
arrow(ax, (X(PI), yb), (X(3 * PI), yb), 'varie', lw=1.4)
text(ax, X(2 * PI), yb - 3.2, r'$+2\pi$', 'varie', 's')
for t in (0, 2 * PI):
    line(ax, [(X(t), Y(1)), (X(t), yt)], 'fixe', lw=0.5, dash=True)
for t in (PI, 3 * PI):
    line(ax, [(X(t), Y(-1)), (X(t), yb)], 'fixe', lw=0.5, dash=True)
text(ax, X(2 * PI) + 12, Y(1) + 8, 'cosinus égaux', 'resultat', 's')
save(fig, '30-024')
