import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(66)
r = 17
def panel(cx, cy, b0, bearing, role, title):
    c = (cx, cy)
    disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.6)
    line(ax, [(cx, cy - r), (cx, cy + r)], 'fixe', lw=0.8); line(ax, [(cx - r, cy), (cx + r, cy)], 'fixe', lw=0.8)
    a = math.radians(bearing); tip = (cx + r*math.sin(a), cy + r*math.cos(a))
    arrow(ax, c, tip, role, lw=1.6)
    lo, hi = sorted([90 - b0, 90 - bearing])
    arc(ax, c, 9, lo, hi, 'varie', lw=1.2)
    text(ax, cx, cy + r + 3.5, 'N', 'encre', 's'); text(ax, cx, cy - r - 3.5, 'S', 'encre', 's')
    text(ax, cx + r + 2.5, cy, 'E', 'resultat', 's')
    text(ax, cx, 62, title, role, 'l')
panel(22, 32, 0, 40, 'sujet', 'N 40° E')
panel(66, 32, 180, 110, 'autre', 'S 70° E')
text(ax, 22 + 4.4, 32 + 12.2, r'$40°$', 'varie', 's')
text(ax, 66 + 11, 32 - 8, r'$70°$', 'varie', 's')
text(ax, 22, 5, 'départ : nord', 'sujet', 's'); text(ax, 66, 5, 'départ : sud', 'autre', 's')
save(fig, '36-128')
