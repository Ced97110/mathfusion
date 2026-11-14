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

fig, ax = canvas(80); cx, cy, R = 42, 38, 28
ucirc(ax, cx, cy, R)
P = pt(cx, cy, R, 120); S = pt(cx, cy, R, 60)
line(ax, [(cx, cy), P], 'sujet', lw=1.4); line(ax, [(cx, cy), S], 'fixe', lw=1.0)
line(ax, [(S[0], cy), S], 'fixe', dash=True); line(ax, [(P[0], cy), P], 'resultat', lw=2.0)
line(ax, [P, S], 'fixe', dash=True)
arcp(ax, cx, cy, 10, 120, 180, 'varie', 1.2); arcp(ax, cx, cy, 14, 0, 120, 'sujet', 0.8)
dot(ax, P, 'sujet'); dot(ax, S, 'fixe')
text(ax, P[0] - 2, P[1] + 3, r'$P$ : 120°', 'sujet', 's', ha='right')
text(ax, S[0] + 2, S[1] + 3, '60°', 'fixe', 's', ha='left')
text(ax, cx - 17, cy + 5, '60°', 'varie', 's')
text(ax, P[0] - 1.5, cy - 4, 'sin 120°', 'resultat', 's', ha='right')
text(ax, 44, 6.5, r'sin 120° = $\sqrt{3}/2$ ≈ 0,866', 'resultat', 'm')
text(ax, 44, 75, 'quadrant II : sinus positif', 'encre', 's')
save(fig, '28-106')
