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

fig, ax = canvas(72); cx, cy, R = 30, 36, 24
ucirc(ax, cx, cy, R)
P = pt(cx, cy, R, 315)
line(ax, [(cx, cy), P], 'sujet', lw=1.4); dot(ax, P, 'sujet')
line(ax, [(cx, cy), (P[0], cy)], 'resultat', lw=1.8); line(ax, [(P[0], cy), P], 'varie', lw=1.8)
arcp(ax, cx, cy, 10, 315, 360, 'varie', 1.0)
text(ax, cx + 6, cy + 3.5, r'$x > 0$', 'resultat', 's', ha='left')
text(ax, P[0] + 2, (cy + P[1]) / 2, r'$y < 0$', 'varie', 's', ha='left')
text(ax, P[0] + 1, P[1] - 3.5, '315° : IV', 'sujet', 's', ha='left')
text(ax, cx + 14, cy + 9, '45°', 'varie', 's', ha='left')
text(ax, 72, 56, 'référence', 'encre', 's'); text(ax, 72, 52, '45°', 'encre', 's')
text(ax, 72, 40, 'tan 45° = 1', 'fixe', 's'); text(ax, 72, 31, 'signe IV : −', 'varie', 's')
text(ax, 72, 22, 'tan 315° = −1', 'resultat', 's', weight='bold')
save(fig, '28-108')
