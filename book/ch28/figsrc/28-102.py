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

fig, ax = canvas(80); cx, cy, R = 44, 36, 28
ucirc(ax, cx, cy, R, ext=1)
line(ax, [(cx, cy - R - 4), (cx, cy + R + 8)], 'varie', lw=1.0, dash=True)
P = pt(cx, cy, R, 130); Q = pt(cx, cy, R, 50)
line(ax, [(cx, cy), P], 'sujet', lw=1.2); line(ax, [(cx, cy), Q], 'resultat', lw=1.2)
arcp(ax, cx, cy, 10, 90, 130, 'sujet'); arcp(ax, cx, cy, 10, 50, 90, 'resultat')
arrow(ax, (P[0] + 3, P[1] + 2), (Q[0] - 3, Q[1] + 2), 'varie', curve=-0.35)
dot(ax, P, 'sujet'); dot(ax, Q, 'resultat')
text(ax, P[0] - 2, P[1] - 3, r'$P$ : $\theta$ = 130°', 'sujet', 's', ha='right')
text(ax, Q[0] + 2, Q[1] - 3, r'2$\alpha-\theta$ = 50°', 'resultat', 's', ha='left')
text(ax, cx - 7, cy + 15.5, '40°', 'sujet', 's', ha='right'); text(ax, cx + 7, cy + 15.5, '40°', 'resultat', 's', ha='left')
text(ax, cx + 2, cy + R + 9, r'droite $\alpha$ = 90°', 'varie', 's', ha='left')
text(ax, 44, 4, 'le reflet garde l’écart, change de côté', 'encre', 's')
save(fig, '28-102')
