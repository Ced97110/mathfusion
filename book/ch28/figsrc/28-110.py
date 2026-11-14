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

fig, ax = canvas(86); cx, cy, R = 44, 50, 28
ucirc(ax, cx, cy, R)
yy = cy - R * 2 / 3; xx = R * (5 ** 0.5) / 3
line(ax, [(cx - R - 3, yy), (cx + R + 3, yy)], 'varie', lw=1.0, dash=True)
P = (cx - xx, yy); Q = (cx + xx, yy)
line(ax, [(cx, cy), P], 'sujet', lw=1.4)
line(ax, [(P[0], cy), P], 'varie', lw=1.8); line(ax, [(cx, cy), (P[0], cy)], 'resultat', lw=1.8)
ax.add_patch(Circle(Q, 1.4, ec=COL['limite'], fc=FILL['limite'], lw=1.0, zorder=4))
dot(ax, P, 'sujet')
text(ax, P[0] - 2, P[1] - 3, r'$P$ : quadrant III', 'sujet', 's', ha='right')
text(ax, Q[0] + 1, Q[1] - 3.5, 'tan < 0 : écarté', 'limite', 's', ha='left')
text(ax, P[0] - 1, cy + 3, r'$x$', 'resultat', 's', ha='right')
text(ax, P[0] - 1.5, (cy + yy) / 2, r'$y = -2/3$', 'varie', 's', ha='right')
text(ax, 44, 80, r'sin $\theta$ = −2/3 et tan $\theta$ > 0', 'encre', 'm')
text(ax, 44, 10, r'cos $\theta = -\sqrt{5}/3$ ≈ −0,745', 'resultat', 'm')
text(ax, 44, 4.5, r'tan $\theta$ ≈ 0,894', 'resultat', 'm')
save(fig, '28-110')
