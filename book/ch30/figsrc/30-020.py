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
ox, oy, ux, uy = 14, 8, 18, 10
for i in range(4):
    line(ax, [(ox + i * ux, oy), (ox + i * ux, oy + 5 * uy)], 'fixe', lw=0.3)
for j in range(6):
    line(ax, [(ox, oy + j * uy), (ox + 3 * ux, oy + j * uy)], 'fixe', lw=0.3)
arrow(ax, (ox - 3, oy), (ox + 3 * ux + 8, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 3), (ox, oy + 5.5 * uy + 6), 'fixe', lw=0.9)
text(ax, ox + 3 * ux + 8, oy - 3.5, '$x$', 'fixe', 's')
text(ax, ox - 4, oy + 5.5 * uy + 6, '$y$', 'fixe', 's')
pts = [(0, 1), (1, 2), (2, 5)]
for (a, b) in pts:
    px, py = ox + a * ux, oy + b * uy
    line(ax, [(px, oy), (px, py)], 'sujet', lw=0.6, dash=True)
    line(ax, [(ox, py), (px, py)], 'sujet', lw=0.6, dash=True)
    dot(ax, px, py, 'sujet', 1.4)
    text(ax, px + 3, py + 3.2, f'({a}, {b})', 'sujet', 's', ha='left')
text(ax, ox + 0.55 * ux, oy + 1.75 * uy, '?', 'fixe', 'l')
text(ax, ox + 1.5 * ux, oy + 3.5 * uy, '?', 'fixe', 'l')
text(ax, ox + 3 * ux, oy + 0.5 * uy, 'trois points', 'sujet', 's', ha='right')
save(fig, '30-020')
