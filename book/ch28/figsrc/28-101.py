import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pt(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def ucirc(ax, cx, cy, R, ext=3):
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.8)
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.6)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.6)
def arcp(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [pt(cx, cy, r, a0 + (a1 - a0) * i / 40) for i in range(41)], role, lw)
def dot(ax, p, role, r=1.1): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
def wedge(ax, cx, cy, R, a0, a1, role):
    poly(ax, [(cx, cy)] + [pt(cx, cy, R, a0 + (a1 - a0) * i / 30) for i in range(31)], role)

fig, ax = canvas(80); cx, cy, R = 44, 40, 28
wedge(ax, cx, cy, R, 0, 90, 'sujet')
ucirc(ax, cx, cy, R)
P = pt(cx, cy, R, 30); P2 = pt(cx, cy, R, 130); P3 = pt(cx, cy, R, 210)
dot(ax, P, 'sujet')
for p in (P2, P3):
    ax.add_patch(Circle(p, 1.4, ec=COL['autre'], fc=FILL['autre'], lw=1.0, zorder=4))
text(ax, P[0] + 2, P[1] + 2.5, '30° : vu', 'sujet', 's', ha='left')
text(ax, P2[0] - 2, P2[1] + 3, '130° : ?', 'autre', 'm', ha='right')
text(ax, P3[0] - 2, P3[1] - 3, '210° : ?', 'autre', 'm', ha='right')
text(ax, cx + 13, cy + 13, 'I', 'sujet', 'l', weight='bold')
text(ax, cx - 13, cy + 13, 'II', 'fixe', 'l'); text(ax, cx - 13, cy - 13, 'III', 'fixe', 'l'); text(ax, cx + 13, cy - 13, 'IV', 'fixe', 'l')
text(ax, 44, 76, 'la figure ne montre que le quadrant I', 'encre', 's')
save(fig, '28-101')
