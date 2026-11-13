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
x0 = 4; u = 40 / (2 * P_)
y = 40
box(ax, x0, y - 4, 40, 8, 'fixe', fill=False, dash=True, lw=0.6, r=0.5)
box(ax, x0, y - 4, 0.898 * u, 8, 'resultat', r=0.5)
text(ax, x0, y + 9, 'un tour entier = 2π ≈ 6,28', 'fixe', 's', ha='left')
text(ax, x0, y - 8, 'f = 1/7 (période 7 s)', 'encre', 's', ha='left')
text(ax, x0, y - 12.5, r'$\omega = 2\pi \times 1/7 \approx 0{,}898$', 'resultat', 's', ha='left')
y = 14
for k in (0, 1): box(ax, x0 + 40 * k, y - 4, 40, 8, 'fixe', fill=False, dash=True, lw=0.6, r=0.5)
box(ax, x0, y - 4, 9.42 * u, 8, 'resultat', r=0.5)
text(ax, x0, y + 8, 'f = 1,5 cycle par seconde', 'encre', 's', ha='left')
text(ax, x0, y - 8, r'$\omega = 2\pi \times 1{,}5 = 9{,}42$', 'resultat', 's', ha='left')
save(fig, '30-158')
