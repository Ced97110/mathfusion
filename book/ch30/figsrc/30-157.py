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
ox, oy, sx, sy = 14, 30, 9, 2.2; w = 2 * P_ / 7
line(ax, [(ox, oy), (ox + 66, oy)], 'fixe'); line(ax, [(ox, oy - 14), (ox, oy + 15)], 'fixe')
line(ax, [(ox, oy + 5 * sy), (ox + 63, oy + 5 * sy)], 'fixe', lw=0.5, dash=True)
curve(ax, lambda t: 5 * np.cos(w * t), 0, 7, ox, oy, sx, sy, 'sujet')
dv = 5 * math.cos(w * 2) * sy
line(ax, [(ox + 18, oy), (ox + 18, oy + dv)], 'resultat', lw=0.8, dash=True)
line(ax, [(ox + 18, oy + dv), (ox + 18, oy - 14)], 'resultat', lw=0.6, dash=True)
disc(ax, ox + 18, oy + dv, 1.3, 'resultat')
text(ax, ox - 1.5, oy + 14, 'd (cm)', 'fixe', 's', ha='right'); text(ax, ox + 20, oy + 14, 'a = 5 cm', 'sujet', 's')
text(ax, ox + 18, oy + 3.2, '2 s', 'fixe', 's'); text(ax, ox + 63, oy - 3.2, '7 s', 'fixe', 's'); text(ax, ox + 71, oy + 3.2, 't (s)', 'fixe', 's')
text(ax, ox + 18, oy - 17, 'd ≈ −1,11 cm', 'resultat', 's')
brace(ax, ox, ox + 63, oy + 17, 'varie', r'un cycle : $\omega=2\pi/7\approx 0{,}898$', down=False)
text(ax, 44, 59, r'$d=a\,\cos(\omega t)$', 'encre', 'l', weight='bold')
save(fig, '30-157')
