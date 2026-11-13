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
cyy = 38
# grand cercle : 120 degrés, hauteur ET position horizontale
c = 30; r = 15
ucirc(ax, c, cyy, r, ext=1.5)
P = pt(c, cyy, r, 120)
line(ax, [(c, cyy), P], 'sujet', lw=1.6); dot(ax, P, 'sujet', 0.9)
line(ax, [(P[0], cyy), P], 'resultat', lw=2.4)
line(ax, [(c, cyy), (P[0], cyy)], 'resultat', lw=2.4)
arrow(ax, (14, 45), (P[0] - 1, 45), 'resultat', lw=0.7)
text(ax, 13, 45, 'hauteur', 'resultat', 's', ha='right')
text(ax, 26, 33.5, 'à gauche', 'resultat', 's')
text(ax, c, 61, '120°', 'sujet', 'm', weight='bold')
text(ax, c, 22, 'hauteur : 17 × sin 120°', 'varie', 's'); text(ax, c, 18, '≈ 14,72 cm', 'resultat', 's', weight='bold')
text(ax, c, 12, 'à gauche : 17 × cos 120°', 'varie', 's'); text(ax, c, 8, '−8,5 cm (en arrière)', 'resultat', 's', weight='bold')
# petit cercle : 210 degrés
c2 = 69; r2 = 11
ucirc(ax, c2, cyy, r2, ext=1.5)
P2 = pt(c2, cyy, r2, 210)
line(ax, [(c2, cyy), P2], 'sujet', lw=1.6); dot(ax, P2, 'sujet', 0.9)
line(ax, [(P2[0], cyy), P2], 'resultat', lw=2.4); line(ax, [(c2, cyy), (P2[0], cyy)], 'fixe', dash=True)
text(ax, c2, 56, '210°', 'sujet', 'm', weight='bold')
text(ax, c2, 22, 'hauteur : 17 × sin 210°', 'varie', 's'); text(ax, c2, 18, '−8,5 cm (sous l’axe)', 'resultat', 's', weight='bold')
text(ax, 44, 67, 'manivelle : 17 cm', 'sujet', 's')
save(fig, '28-109')
