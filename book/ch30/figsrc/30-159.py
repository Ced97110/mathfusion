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
fig, ax = canvas(44)
x0, y, u = 6, 26, 7
line(ax, [(x0, y), (x0 + 9.42 * u, y)], 'fixe')
for v, lab in ((0, '0'), (2 * P_, '6,28'), (3 * P_, '9,42')):
    line(ax, [(x0 + v * u, y - 1.2), (x0 + v * u, y + 1.2)], 'fixe'); text(ax, x0 + v * u, y - 3.4, lab, 'fixe', 's')
brace(ax, x0, x0 + 2 * P_ * u, y + 2, 'sujet', 'un cycle : 6,28', down=False)
brace(ax, x0 + 2 * P_ * u, x0 + 3 * P_ * u, y + 2, 'varie', 'demi-cycle : 3,14', down=False)
brace(ax, x0, x0 + 3 * P_ * u, y - 8, 'resultat', 'en 1 s : 9,42')
text(ax, 80, y, r'$=\omega$', 'resultat', 'xl'); text(ax, 80, y - 7, 'oméga', 'resultat', 's')
save(fig, '30-159')
