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
ox, oy, s = 44, 30, 9
line(ax, [(ox - 40, oy), (ox + 40, oy)], 'fixe'); line(ax, [(ox, oy - 14), (ox, oy + 14)], 'fixe')
curve(ax, np.sin, -4.2, 4.2, ox, oy, s, s, 'sujet')
Px, Py = ox + P_ / 2 * s, oy + s; Qx, Qy = ox - P_ / 2 * s, oy - s
line(ax, [(Px, Py), (Qx, Qy)], 'fixe', lw=0.7, dash=True)
R = math.hypot(Px - ox, Py - oy); a0 = math.degrees(math.atan2(Py - oy, Px - ox))
arc(ax, ox, oy, R, a0, a0 + 180, 'varie')
disc(ax, ox, oy, 0.9, 'fixe'); disc(ax, Px, Py, 1.3, 'sujet'); disc(ax, Qx, Qy, 1.3, 'resultat')
text(ax, ox + 2.5, oy - 2.8, 'O', 'fixe', 's')
text(ax, Px + 3, Py + 3, 'hauteur 1', 'sujet', 's', ha='left'); text(ax, Qx - 3, Qy - 3.5, 'hauteur −1', 'resultat', 's', ha='right')
text(ax, ox, oy + 22, 'demi-tour autour de O', 'varie', 's')
text(ax, ox, oy - 19, 'le point tourné est sur la courbe', 'resultat', 's')
save(fig, '30-154')
