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

fig, ax = canvas(80); cx, cy, R = 40, 40, 26
ucirc(ax, cx, cy, R)
P = pt(cx, cy, R, 30); Q = pt(cx, cy, R, -30)
line(ax, [(cx, cy), P], 'sujet'); line(ax, [(cx, cy), Q], 'varie')
line(ax, [(P[0], cy), P], 'fixe', dash=True); line(ax, [(Q[0], cy), Q], 'fixe', dash=True)
line(ax, [(cx, cy), (P[0], cy)], 'resultat', lw=2.0)
arcp(ax, cx, cy, 9, 0, 30, 'sujet'); arcp(ax, cx, cy, 9, -30, 0, 'varie')
dot(ax, P, 'sujet'); dot(ax, Q, 'varie')
text(ax, P[0] + 2, P[1] + 3, r'$P$ : 30°', 'sujet', 's', ha='left')
text(ax, Q[0] + 2, Q[1] - 3, r'$P\prime$ : −30°', 'varie', 's', ha='left')
text(ax, cx + (P[0] - cx) / 2, cy + 3.2, 'cos', 'resultat', 's')
text(ax, 44, 8, 'même abscisse : 0,866', 'resultat', 'm')
text(ax, 44, 3, 'cos(−30°) = cos 30°', 'resultat', 's')
save(fig, '28-098')
