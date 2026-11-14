import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, tip=False, dash=False):
    n = max(2, int(abs(a1 - a0) / 3) + 1)
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / (n - 1)) for i in range(n)], role, lw, dash)
    if tip:
        s = 1 if a1 > a0 else -1
        arrow(ax, P(cx, cy, R, a1 - s * 6), P(cx, cy, R, a1), role, lw)
def dot(ax, x, y, role, r=1.2): disc(ax, x, y, r, role)
def frame(ax, cx, cy, R, vert=True):
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.8)
    line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5)
    if vert: line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)

fig, ax = canvas(62)
y = 40
f = numberline(ax, 8, 80, y, 0, 180, step=10, labels=False, arrow_right=False)
line(ax, [(f(90), y - 5), (f(90), y + 10)], 'fixe', dash=True)
text(ax, f(90), y + 13, 'axe du reflet', 'fixe', 's')
dot(ax, f(40), y, 'sujet', 1.6); dot(ax, f(140), y, 'varie', 1.6)
text(ax, f(40), y + 6, '$\\alpha$ = 40°', 'sujet', 's')
text(ax, f(140), y + 6, '180° − $\\alpha$ = 140°', 'varie', 's')
brace(ax, f(0), f(40), y - 5, 'sujet', label='40°')
brace(ax, f(140), f(180), y - 5, 'varie', label='40°')
brace(ax, f(0), f(180), y - 13, 'fixe', label='180° : un demi-tour')
save(fig, '32-047')
