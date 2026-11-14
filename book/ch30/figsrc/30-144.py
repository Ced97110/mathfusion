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
fig, ax = canvas(70)
x0 = 22; sx = 40 / (4 * P_); amp = 5
text(ax, x0 + 20, 65, 'même fenêtre de lecture', 'fixe', 's')
for i, (B, T) in enumerate([(1, '6,28'), (0.1, '62,8'), (0.01, '628'), (0.001, '6 283')]):
    y = 54 - i * 14
    box(ax, x0 - 1.5, y - 6.5, 43, 13, 'fixe', fill=False, dash=True, lw=0.5)
    curve(ax, lambda x, B=B: np.sin(B * x), 0, 4 * P_, x0, y, sx, amp, 'sujet')
    text(ax, 4, y, ('B = ' + str(B)).replace('.', ','), 'varie', 's', ha='left')
    text(ax, 66, y, 'période ' + T, 'resultat', 's', ha='left')
save(fig, '30-144')
