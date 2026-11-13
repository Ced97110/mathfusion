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

fig, ax = canvas(88)
xs = [14, 34, 54, 74]; names = ['ramener', 'quadrant', 'calculer', 'signe']
for i, (x, n) in enumerate(zip(xs, names)):
    role = 'limite' if i == 1 else ('fixe' if i > 1 else 'sujet')
    box(ax, x - 9.5, 72, 19, 10, role, label=f'{i + 1}. {n}', size='s', dash=(i > 1))
    if i < 3: arrow(ax, (x + 9.5, 77), (xs[i + 1] - 9.5, 77), 'fixe' if i > 0 else 'varie')
cx, cy, R = 34, 36, 22
ucirc(ax, cx, cy, R, ext=3)
P = pt(cx, cy, R, 90)
line(ax, [(cx, cy), P], 'sujet', lw=1.6); dot(ax, P, 'sujet')
arcp(ax, cx, cy, 8, 0, 90, 'varie')
text(ax, cx + 4, cy + 14, '90°', 'varie', 's', ha='left')
text(ax, cx + 3, P[1] + 3, r'$P$ (0 ; 1)', 'sujet', 's', ha='left')
arrow(ax, (xs[1], 71), (xs[1], P[1] + 8), 'limite')
text(ax, cx + 24, cy - 5, 'sur l’axe :', 'limite', 's', ha='left'); text(ax, cx + 24, cy - 9, 'aucun quadrant', 'limite', 's', ha='left')
text(ax, 14, 53, r'cos 90° ?', 'encre', 'm')
save(fig, '28-105')
