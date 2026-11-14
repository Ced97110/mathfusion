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
fig, ax = canvas(64)
ox, oy, sx, sy = 10, 32, 11, 4.5
line(ax, [(ox, oy), (ox + 2 * P_ * sx + 3, oy)], 'fixe'); line(ax, [(ox, oy - 16), (ox, oy + 17)], 'fixe')
curve(ax, lambda x: 3 * np.sin(x), 0, 2 * P_, ox, oy, sx, sy, 'fixe', lw=1.1, dash=True)
curve(ax, lambda x: -3 * np.sin(x), 0, 2 * P_, ox, oy, sx, sy, 'sujet')
disc(ax, ox + P_ / 2 * sx, oy + 3 * sy, 1.2, 'fixe'); disc(ax, ox + 3 * P_ / 2 * sx, oy + 3 * sy, 1.2, 'sujet')
arrow(ax, (ox + P_ / 2 * sx + 2, oy + 3 * sy + 3), (ox + 3 * P_ / 2 * sx - 2, oy + 3 * sy + 3), 'varie')
text(ax, ox + P_ * sx, oy + 3 * sy + 6.5, 'décalage d’une demi-période', 'varie', 's')
text(ax, ox + P_ / 2 * sx, oy + 3 * sy - 3.5, r'$3\sin x$', 'fixe', 's')
text(ax, ox + P_ / 2 * sx + 2, oy - 3 * sy - 4, r'$-3\sin x$', 'sujet', 's')
text(ax, 44, 7, r'$-3\sin x = 3\sin(x-\pi)$', 'resultat', 'm')
save(fig, '30-148')
