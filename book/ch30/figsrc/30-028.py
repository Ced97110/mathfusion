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
x0, u = 6, 15.0
rows = [(r'$p=4\pi$ : pas le plus petit', 'fixe', 4 * PI / PI), (r'$p=2\pi$ : la période', 'resultat', 2.0), (r'$p=\pi$ : échoue en $\pi/2$', 'limite', 1.0)]
line(ax, [(x0, 8), (x0, 54)], 'fixe', lw=0.8, dash=True)
text(ax, x0, 58, '$x$', 'fixe', 's')
for k, (lab, role, L) in enumerate(rows):
    y = 44 - k * 17
    text(ax, x0 + 2, y + 6, lab, role, 's', ha='left')
    arrow(ax, (x0, y), (x0 + L * u - 0.5, y), role, lw=1.6)
    dot(ax, x0 + L * u, y, role, 1.2)
save(fig, '30-028')
