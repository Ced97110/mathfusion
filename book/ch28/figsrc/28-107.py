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
ucirc(ax, cx, cy, R)
P = pt(cx, cy, R, 210); S = pt(cx, cy, R, 30)
line(ax, [(cx, cy), P], 'sujet', lw=1.4); line(ax, [(cx, cy), S], 'fixe', lw=1.0)
line(ax, [(P[0], cy), P], 'fixe', dash=True); line(ax, [(S[0], cy), S], 'fixe', dash=True)
line(ax, [(cx, cy), (P[0], cy)], 'resultat', lw=2.2)
arcp(ax, cx, cy, 12, 180, 210, 'varie', 1.4)
dot(ax, P, 'sujet'); dot(ax, S, 'fixe')
text(ax, P[0] - 1.5, P[1] - 3, r'$P$ : 210°', 'sujet', 's', ha='right')
text(ax, S[0] + 2, S[1] + 3, '30°', 'fixe', 's', ha='left')
text(ax, cx - 19, cy - 4.5, '30°', 'varie', 's')
text(ax, cx - 12, cy + 3, 'cos 210°', 'resultat', 's')
text(ax, 44, 6.5, r'cos 210° = $-\sqrt{3}/2$', 'resultat', 'm')
text(ax, 44, 76, 'quadrant III : cosinus négatif', 'encre', 's')
save(fig, '28-107')
