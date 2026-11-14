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

fig, ax = canvas(80); cx, cy, R = 38, 40, 26
ucirc(ax, cx, cy, R)
P = pt(cx, cy, R, 30); Q = pt(cx, cy, R, -30)
line(ax, [(cx, cy), P], 'sujet'); line(ax, [(cx, cy), Q], 'varie')
line(ax, [(P[0], cy), P], 'sujet', lw=1.8); line(ax, [(Q[0], cy), Q], 'varie', lw=1.8)
arcp(ax, cx, cy, 9, 0, 30, 'sujet'); arcp(ax, cx, cy, 9, -30, 0, 'varie')
dot(ax, P, 'sujet'); dot(ax, Q, 'varie')
text(ax, cx + 13, cy + 3.6, r'$\theta$', 'sujet', 's'); text(ax, cx + 13, cy - 3.6, r'$-\theta$', 'varie', 's')
text(ax, P[0] + 2, P[1] + 3, r'$P$ : 30°', 'sujet', 's', ha='left')
text(ax, Q[0] + 2, Q[1] - 3, r'$P\prime$ : −30°', 'varie', 's', ha='left')
text(ax, P[0] + 2, (cy + P[1]) / 2 - 1, 'sin 30° = 0,5', 'sujet', 's', ha='left')
text(ax, Q[0] + 2, (cy + Q[1]) / 2 + 1, 'sin(−30°) = −0,5', 'varie', 's', ha='left')
text(ax, 44, 5, r'même longueur, signe contraire', 'encre', 's')
save(fig, '28-097')
