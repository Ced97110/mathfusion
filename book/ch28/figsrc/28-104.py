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

fig, ax = canvas(70)
cols = [(12, 'I', r'$\theta$', 40, 40), (33, 'II', r'180° − $\theta$', 130, 50), (54, 'III', r'$\theta$ − 180°', 210, 30), (75, 'IV', r'360° − $\theta$', 315, 45)]
r = 8; cyy = 40
for c, q, f, th, ref in cols:
    ucirc(ax, c, cyy, r, ext=1.5)
    P = pt(c, cyy, r, th)
    line(ax, [(c, cyy), P], 'sujet', lw=1.2); dot(ax, P, 'sujet', 0.9)
    if th < 90: arcp(ax, c, cyy, 4.5, 0, th, 'resultat', 1.6)
    elif th < 180: arcp(ax, c, cyy, 4.5, th, 180, 'resultat', 1.6)
    elif th < 270: arcp(ax, c, cyy, 4.5, 180, th, 'resultat', 1.6)
    else: arcp(ax, c, cyy, 4.5, th, 360, 'resultat', 1.6)
    text(ax, c, 60, q, 'sujet', 'l', weight='bold')
    text(ax, c, 27, f, 'varie', 's')
    text(ax, c, 21, f'{th}° → {ref}°', 'resultat', 's')
text(ax, 44, 11, '400° donne 400 : faux', 'limite', 'm')
text(ax, 44, 5.5, 'retirer un tour : 40°', 'encre', 's')
save(fig, '28-104')
