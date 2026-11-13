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

fig, ax = canvas(72)
f = numberline(ax, 14, 74, 54, -1, 1, step=1, arrow_right=False)
v = (5 ** 0.5) / 3
for s, role in [(-1, 'sujet'), (1, 'fixe')]:
    ax.add_patch(Circle((f(s * v), 54), 1.5, ec=COL[role], fc=COL[role], zorder=4))
text(ax, f(-v), 62, r'$-\sqrt{5}/3$', 'sujet', 's'); text(ax, f(v), 62, r'$\sqrt{5}/3$', 'fixe', 's')
box(ax, 29, 24, 30, 9, 'resultat', label=r'$x^2$ = 5/9', size='m')
arrow(ax, (f(-v), 51), (36, 34), 'varie'); arrow(ax, (f(v), 51), (52, 34), 'varie')
text(ax, 14, 41, 'au carré', 'varie', 's'); text(ax, 74, 41, 'au carré', 'varie', 's')
text(ax, 44, 17, 'le carré efface le signe', 'encre', 's')
text(ax, 44, 9, 'quadrant III : x < 0', 'sujet', 'm', weight='bold')
text(ax, 44, 3.5, 'on garde le négatif', 'sujet', 's')
save(fig, '28-112')
