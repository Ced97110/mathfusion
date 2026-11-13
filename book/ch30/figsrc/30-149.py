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
cx, cy, r = 36, 38, 24; a = math.radians(30)
circ(ax, cx, cy, r)
line(ax, [(cx - r - 3, cy), (cx + r + 3, cy)], 'fixe', lw=0.6); line(ax, [(cx, cy - r - 3), (cx, cy + r + 3)], 'fixe', lw=0.6)
Px, Py = cx + r * math.cos(a), cy + r * math.sin(a); Qy = cy - r * math.sin(a)
line(ax, [(cx, cy), (Px, Py)], 'sujet', lw=1.2); line(ax, [(cx, cy), (Px, Qy)], 'autre', lw=1.2)
line(ax, [(Px, Qy), (Px, Py)], 'varie', lw=0.9, dash=True)
arc(ax, cx, cy, 9, 0, 30, 'varie', head=False); arc(ax, cx, cy, 9, 0, -30, 'varie', head=False)
text(ax, cx + 14, cy + 4.5, 'x', 'varie', 's'); text(ax, cx + 14, cy - 4.5, '−x', 'varie', 's')
disc(ax, Px, Py, 1.3, 'sujet'); disc(ax, Px, Qy, 1.3, 'autre')
text(ax, Px + 3, Py + 3, 'P : (0,866 ; 0,5)', 'sujet', 's', ha='left')
text(ax, Px + 3, Qy - 3, 'P′ : (0,866 ; −0,5)', 'autre', 's', ha='left')
text(ax, Px + 3, cy - 4, 'reflet', 'varie', 's', ha='left')
text(ax, 44, 6, 'même abscisse, hauteur ±0,5', 'resultat', 's')
save(fig, '30-149')
