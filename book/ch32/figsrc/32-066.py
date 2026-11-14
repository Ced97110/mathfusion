import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(80); cx, cy, R = 40, 38, 22
uc(ax, cx, cy, R)
a = math.degrees(math.atan(0.75)); d = (math.cos(math.radians(a)), math.sin(math.radians(a)))
P = pp(cx, cy, R, a); Q = pp(cx, cy, R, a + 180)
line(ax, [(cx - 1.15 * R * d[0], cy - 1.15 * R * d[1]), (cx + 1.25 * R * d[0], cy + 1.25 * R * d[1])], 'sujet', lw=1.3)
line(ax, [(cx, cy), (cx + R, cy)], 'varie', lw=1.6, dash=True)
line(ax, [(cx + R, cy), (cx + R, cy + 0.75 * R)], 'varie', lw=1.6, dash=True)
dot(ax, P, 'resultat', 1.6); dot(ax, Q, 'resultat', 1.6)
text(ax, P[0] - 1, P[1] + 3.8, 'P', 'resultat', 'l', weight='bold')
text(ax, Q[0] - 3, Q[1] - 3.2, 'Q', 'resultat', 'l', weight='bold')
text(ax, cx + R / 2, cy - 3.5, 'avance 1', 'varie', 's')
text(ax, cx + R + 1.8, cy + 8, 'monte 0,75', 'varie', 's', ha='left')
text(ax, W / 2, 74, 'P et Q : pente de OP = 0,75', 'sujet', 'm')
save(fig, '32-066')
