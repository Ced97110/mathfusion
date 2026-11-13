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
cx, cy, r = 44, 38, 22
circ(ax, cx, cy, r)
line(ax, [(cx - r - 3, cy), (cx + r + 3, cy)], 'fixe', lw=0.6); line(ax, [(cx, cy - r - 3), (cx, cy + r + 3)], 'fixe', lw=0.6)
pts = {}
for name, deg, role in (('A', 30, 'sujet'), ('B', -30, 'varie'), ('C', 150, 'autre')):
    a = math.radians(deg); x, y = cx + r * math.cos(a), cy + r * math.sin(a); pts[name] = (x, y)
    line(ax, [(cx, cy), (x, y)], role, lw=1.0); line(ax, [(x, cy), (x, y)], role, lw=2.0); disc(ax, x, y, 1.3, role)
line(ax, [pts['C'], pts['A']], 'fixe', lw=0.7, dash=True)
text(ax, 44, 53.5, 'même hauteur 0,5', 'resultat', 's')
text(ax, pts['A'][0] + 3, pts['A'][1] + 4, '30° : 0,5', 'sujet', 's', ha='left')
text(ax, pts['B'][0] + 3, pts['B'][1] - 4, '−30° : −0,5', 'varie', 's', ha='left')
text(ax, pts['C'][0] - 3, pts['C'][1] + 4, '150° : 0,5', 'autre', 's', ha='right')
arrow(ax, (70, pts['B'][1] + 1), (70, pts['A'][1] - 1), 'fixe', both=True); text(ax, 72, 38, 'opposées', 'fixe', 's', ha='left')
save(fig, '30-151')
