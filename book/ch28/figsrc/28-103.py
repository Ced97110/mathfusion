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

fig, ax = canvas(80); cx, cy, R = 44, 42, 28
ucirc(ax, cx, cy, R)
P = pt(cx, cy, R, 210)
line(ax, [(cx, cy), P], 'sujet', lw=1.4); dot(ax, P, 'sujet')
arcp(ax, cx, cy, 8, 0, 210, 'varie', lw=1.0)
arcp(ax, cx, cy, 14, 180, 210, 'resultat', lw=1.8)
text(ax, cx + 4, cy + 11, r'$\theta$ = 210°', 'varie', 's', ha='left')
text(ax, cx - 21, cy - 5.5, '30°', 'resultat', 'm', weight='bold')
text(ax, P[0] + 1, P[1] - 4, 'côté final', 'sujet', 's', ha='left')
text(ax, cx - R - 1, cy + 3, '180°', 'fixe', 's', ha='right')
text(ax, 44, 76, 'angle de référence', 'resultat', 'l', weight='bold')
text(ax, 44, 70.5, 'entre le côté final et l’axe x', 'encre', 's')
text(ax, cx + R + 1, cy + 3, '0°', 'fixe', 's', ha='left')
save(fig, '28-103')
