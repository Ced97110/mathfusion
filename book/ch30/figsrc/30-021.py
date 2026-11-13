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
cx, cy, r = 12, 34, 26
t = np.linspace(0, PI / 2, 100)
ax.plot(cx + r * np.cos(t), cy + r * np.sin(t), color=COL['sujet'], lw=1.8, zorder=3)
line(ax, [(cx, cy), (cx + r, cy)], 'fixe'); line(ax, [(cx, cy), (cx, cy + r)], 'fixe')
tt = np.linspace(0, PI / 2, 40); ax.plot(cx + 5 * np.cos(tt), cy + 5 * np.sin(tt), color=COL['fixe'], lw=0.8)
text(ax, cx + 11, cy + 11, '90°', 'fixe', 's')
text(ax, cx + r / 2, cy - 3.5, 'rayon 1', 'fixe', 's')
text(ax, cx + 20, cy + 26.5, 'arc ≈ 1,57', 'sujet', 's', ha='left')
box(ax, 50, 44, 36, 8, 'fixe', label='degrés : 90, à convertir', size='s')
box(ax, 50, 31, 36, 8, 'resultat', label='radians : 1,57 tel quel', size='s')
f = numberline(ax, 12, 56, 12, 0, 2, 1, role='fixe')
ax.plot([f(0), f(1.57)], [12, 12], color=COL['sujet'], lw=3.2, zorder=3, solid_capstyle='butt')
text(ax, (f(0) + f(1.57)) / 2, 18.5, 'même longueur : 1,57', 'sujet', 's')
save(fig, '30-021')
