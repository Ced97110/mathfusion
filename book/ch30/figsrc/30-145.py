import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P_ = math.pi
def curve(ax, f, a, b, ox, oy, sx, sy, role, lw=1.4, dash=False, n=240):
    xs = np.linspace(a, b, n); line(ax, [(ox + x * sx, oy + f(x) * sy) for x in xs], role, lw, dash)
def circ(ax, cx, cy, r, role='fixe', lw=0.9):
    t = np.linspace(0, 2 * P_, 200); line(ax, [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in t], role, lw)
def arc(ax, cx, cy, r, a0, a1, role, head=True, lw=1.0):
    t = np.linspace(math.radians(a0), math.radians(a1), 60); pts = [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in t]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw=lw)
fig, ax = canvas(66)
ox, oy, sx, sy = 10, 30, 11, 12
line(ax, [(ox, oy), (ox + 2 * P_ * sx + 3, oy)], 'fixe'); line(ax, [(ox, oy - 15), (ox, oy + 15)], 'fixe')
for s in (1, -1):
    line(ax, [(ox, oy + s * sy), (ox + 2 * P_ * sx, oy + s * sy)], 'fixe', lw=0.5, dash=True)
text(ax, ox - 1.5, oy + sy, '1', 'fixe', 's', ha='right'); text(ax, ox - 1.5, oy - sy, '−1', 'fixe', 's', ha='right')
curve(ax, np.sin, 0, 2 * P_, ox, oy, sx, sy, 'fixe', lw=1.1, dash=True)
curve(ax, lambda x: -np.sin(x), 0, 2 * P_, ox, oy, sx, sy, 'sujet')
for xv in (P_ / 2, 3 * P_ / 2):
    disc(ax, ox + xv * sx, oy + math.sin(xv) * sy, 1.1, 'fixe'); disc(ax, ox + xv * sx, oy - math.sin(xv) * sy, 1.1, 'sujet')
text(ax, ox + P_ / 2 * sx, oy - 3.2, '1,571', 'fixe', 's'); text(ax, ox + 3 * P_ / 2 * sx, oy + 3.2, '4,712', 'fixe', 's')
text(ax, ox + P_ / 2 * sx, oy + sy + 4, r'$\sin x$', 'fixe', 's')
text(ax, ox + P_ / 2 * sx, oy - sy - 4, r'$-\sin x$', 'sujet', 's')
text(ax, 44, 6, r'$A=-1$ : amplitude $|A|=1$', 'resultat', 'm')
save(fig, '30-145')
