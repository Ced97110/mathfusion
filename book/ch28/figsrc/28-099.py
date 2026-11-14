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

fig, ax = canvas(88); cx, cy, R = 44, 48, 26
a = R * 0.866; b = R * 0.5
for sx, sy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
    poly(ax, [(cx, cy), (cx + sx * a, cy), (cx + sx * a, cy + sy * b), (cx, cy + sy * b)], 'fixe')
ucirc(ax, cx, cy, R)
for ang, s, role, dx, dy, ha in [(30, '+0,5', 'resultat', 2, 2.5, 'left'), (150, '+0,5', 'resultat', -2, 2.5, 'right'),
                           (210, '−0,5', 'varie', -2, -2.5, 'right'), (330, '−0,5', 'varie', 2, -2.5, 'left')]:
    p = pt(cx, cy, R, ang); dot(ax, p, 'sujet')
    text(ax, p[0] + dx, p[1] + dy, s, role, 'm', ha=ha, weight='bold')
text(ax, 44, 84, r'sinus des points à 30°, 150°,', 'encre', 's')
text(ax, 44, 80, r'210° et 330°', 'encre', 's')
text(ax, 22, 7, 'valeur : rectangle gris', 'fixe', 's')
text(ax, 66, 7, 'signe : quadrant', 'varie', 's')
save(fig, '28-099')
