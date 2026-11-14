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
oy = 30
# panneau cosinus
ox, sx, sy = 22, 36 / (2 * P_), 14
line(ax, [(ox - 20, oy), (ox + 20, oy)], 'fixe'); line(ax, [(ox, oy - 8), (ox, oy + 18)], 'fixe')
curve(ax, np.cos, -P_, P_, ox, oy, sx, sy, 'sujet')
yv = oy + math.cos(1) * sy
line(ax, [(ox - sx, yv), (ox + sx, yv)], 'resultat', lw=0.8, dash=True)
for s in (-1, 1):
    disc(ax, ox + s * sx, yv, 1.2, 'resultat'); text(ax, ox + s * sx, oy - 3.2, '1' if s > 0 else '−1', 'fixe', 's')
text(ax, ox, oy + 22, r'$\cos x$', 'sujet', 'm'); text(ax, ox, oy - 12, 'en 1 et −1 : 0,5403', 'resultat', 's')
# panneau parabole
ox, sx, sy = 66, 9, 3.5
line(ax, [(ox - 20, oy), (ox + 20, oy)], 'fixe'); line(ax, [(ox, oy - 8), (ox, oy + 18)], 'fixe')
curve(ax, lambda x: x * x, -2, 2, ox, oy, sx, sy, 'autre')
yv = oy + sy
line(ax, [(ox - sx, yv), (ox + sx, yv)], 'resultat', lw=0.8, dash=True)
for s in (-1, 1):
    disc(ax, ox + s * sx, yv, 1.2, 'resultat'); text(ax, ox + s * sx, oy - 3.2, '1' if s > 0 else '−1', 'fixe', 's')
text(ax, ox, oy + 22, r'$x^2$', 'autre', 'm'); text(ax, ox, oy - 12, 'en 1 et −1 : 1', 'resultat', 's')
save(fig, '30-152')
