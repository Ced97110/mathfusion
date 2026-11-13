import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(88)
cx, cy, R = 44, 44, 24
circ(ax, cx, cy, R, ext=2)
P = lambda u, v: (cx + R * u, cy + R * v)
line(ax, [P(1.5, -0.5), P(-0.5, 1.5)], 'sujet', lw=1.2)
line(ax, [P(0.5, -1.5), P(-1.5, 0.5)], 'limite', lw=1.2, dash=True)
for (u, v), r in [((0, 1), 'resultat'), ((1, 0), 'resultat'), ((-1, 0), 'limite'), ((0, -1), 'limite')]:
    dot(ax, *P(u, v), r, 1.6)
text(ax, 47, 73, r'$A$ 90°', 'resultat', 's', ha='left')
text(ax, 72, 49, r'$B$ 0°', 'resultat', 's', ha='left')
text(ax, 18, 38, 'C 180°\nen trop', 'limite', 's', ha='right')
text(ax, 40, 14, 'D 270° en trop', 'limite', 's', ha='right')
text(ax, 30, 80, r'$x+y=1$', 'sujet', 's', ha='right')
text(ax, 59, 9, r'$x+y=-1$', 'limite', 's', ha='left')
text(ax, 44, 85, 'x = position horizontale, y = hauteur', 'encre', 's')
text(ax, 44, 2.5, 'après le carré : x + y = 1 ou x + y = −1', 'encre', 's')
save(fig, '32-132')
