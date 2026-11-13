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
cx, cy, r = 30, 40, 24
circ(ax, cx, cy, r)
ax_x = 66
line(ax, [(ax_x, cy - r), (ax_x, cy + r)], 'resultat', lw=3.0)
arrow(ax, (ax_x, cy + r), (ax_x, cy + 1.25 * r + 5), 'fixe', lw=0.8)
for h in (0.9, 0.5, -0.3):
    yy = cy + h * r; xx = cx + np.sqrt(r * r - (h * r) ** 2)
    line(ax, [(xx, yy), (ax_x, yy)], 'resultat', lw=0.6, dash=True)
    dot(ax, xx, yy, 'resultat'); dot(ax, ax_x, yy, 'resultat', 1.4)
    text(ax, ax_x + 3.5, yy, f'{h}'.replace('.', ',').replace('-', '\u2212'), 'resultat', 's', ha='left')
yy = cy + 1.2 * r
line(ax, [(cx - 8, yy), (ax_x, yy)], 'limite', lw=0.7, dash=True)
dot(ax, ax_x, yy, 'limite', 1.4)
text(ax, ax_x + 3.5, yy, '1,2', 'limite', 's', ha='left')
text(ax, cx - 14, yy + 3.5, 'jamais atteinte', 'limite', 's', ha='left')
text(ax, 83, cy, r'$[-1,\ 1]$', 'resultat', 's', rot=90)
save(fig, '30-030')
