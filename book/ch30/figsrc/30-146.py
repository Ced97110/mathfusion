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
ox, oy, sx, sy = 12, 33, 7, 12
line(ax, [(ox, oy), (ox + 2 * P_ * sx + 3, oy)], 'fixe'); line(ax, [(ox, oy - 15), (ox, oy + 15)], 'fixe')
for s in (1, -1):
    line(ax, [(ox, oy + s * sy), (80, oy + s * sy)], 'fixe', lw=0.5, dash=True)
text(ax, ox - 1.5, oy + sy, '1', 'fixe', 's', ha='right'); text(ax, ox - 1.5, oy - sy, '−1', 'fixe', 's', ha='right')
curve(ax, lambda x: -np.sin(x), 0, 2 * P_, ox, oy, sx, sy, 'sujet')
text(ax, ox + P_ / 2 * sx, oy - sy - 4, r'$-\sin x$', 'sujet', 's')
arrow(ax, (60, oy - sy), (60, oy + sy), 'varie', both=True); text(ax, 62, oy, 'écart 2', 'varie', 's', ha='left')
arrow(ax, (77, oy), (77, oy + sy), 'resultat'); text(ax, 77, oy + sy + 4, 'moitié : 1', 'resultat', 's')
arrow(ax, (77, oy), (77, oy - sy), 'limite'); text(ax, 77, oy - sy - 4, 'pas −1', 'limite', 's')
text(ax, 40, 5, 'amplitude = moitié de l’écart', 'encre', 's')
save(fig, '30-146')
