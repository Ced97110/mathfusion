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
fig, ax = canvas(62)
ox, oy, sx, sy = 38, 34, 24, 6
line(ax, [(ox - 29, oy), (ox + 29, oy)], 'fixe'); line(ax, [(ox, oy - 17), (ox, oy + 17)], 'fixe')
curve(ax, np.tan, -1.2, 1.2, ox, oy, sx, sy, 'sujet')
yv = math.tan(1) * sy
line(ax, [(ox - sx, oy - yv), (ox + sx, oy + yv)], 'fixe', lw=0.7, dash=True)
disc(ax, ox + sx, oy + yv, 1.3, 'sujet'); disc(ax, ox - sx, oy - yv, 1.3, 'resultat'); disc(ax, ox, oy, 0.9, 'fixe')
text(ax, ox + sx + 3, oy + yv + 1, 'tan 1 ≈ 1,5574', 'sujet', 's', ha='left')
text(ax, ox - sx - 1, oy - yv - 4.5, 'tan(−1) ≈ −1,5574', 'resultat', 's', ha='left')
text(ax, ox, oy + 13, 'demi-tour autour de O', 'varie', 's')
save(fig, '30-155')
