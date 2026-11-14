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
fig, ax = canvas(72)
rest = 30; top = 68; bh, bw = 8, 12
line(ax, [(2, rest), (86, rest)], 'fixe', lw=0.6, dash=True)
line(ax, [(4, top), (84, top)], 'fixe', lw=1.4)
for cx, up, lab, flab, f in ((14, -10, 'écart 5 cm ↓', 'force ↑', 8), (42, 10, 'écart 5 cm ↑', 'force ↓', 8), (68, 20, 'écart 10 cm ↑', 'force ↓ ×2', 16)):
    yc = rest + up; ybt = yc + bh / 2; n = 8; L = top - ybt
    pts = [(cx, top)] + [(cx + (2.5 if i % 2 else -2.5), top - (i - 0.5) * L / n) for i in range(1, n + 1)] + [(cx, ybt)]
    line(ax, pts, 'fixe', lw=0.9)
    box(ax, cx - bw / 2, yc - bh / 2, bw, bh, 'sujet')
    text(ax, cx, 9, lab, 'sujet', 's'); text(ax, cx, 4, flab, 'varie', 's')
    arrow(ax, (cx + 9, rest), (cx + 9, yc), 'sujet', both=True)
    arrow(ax, (cx - 9, yc), (cx - 9, yc + (f if up < 0 else -f)), 'varie', lw=1.6)
text(ax, 84, rest + 2.5, 'repos', 'fixe', 's', ha='right')
save(fig, '30-156')
