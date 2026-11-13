import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
h = 6
xs = [14, 35, 56, 77]
p = (3.4, 1.6)
def sq(cx, cy, role): poly(ax, [(cx-h, cy-h), (cx+h, cy-h), (cx+h, cy+h), (cx-h, cy+h)], role)
text(ax, 44, 60, 'déterminant 1 : 4 rotations', 'sujet', 'm')
for k, cx in enumerate(xs):
    cy = 50; sq(cx, cy, 'sujet')
    a = math.radians(90*k)
    q = (p[0]*math.cos(a) - p[1]*math.sin(a), p[0]*math.sin(a) + p[1]*math.cos(a))
    disc(ax, cx + q[0], cy + q[1], 1.3, 'varie')
    text(ax, cx, 41, ['0°', '90°', '180°', '270°'][k], 'sujet', 's')
text(ax, 44, 33, r'déterminant $-1$ : 4 réflexions', 'autre', 'm')
refl = [lambda x, y: (-x, y), lambda x, y: (x, -y), lambda x, y: (y, x), lambda x, y: (-y, -x)]
axes = [((0, -7.5), (0, 7.5)), ((-7.5, 0), (7.5, 0)), ((-7.5, -7.5), (7.5, 7.5)), ((-7.5, 7.5), (7.5, -7.5))]
for k, cx in enumerate(xs):
    cy = 21; sq(cx, cy, 'autre')
    (a0, a1) = axes[k]
    line(ax, [(cx + a0[0], cy + a0[1]), (cx + a1[0], cy + a1[1])], 'varie', dash=True)
    disc(ax, cx + p[0], cy + p[1], 1.3, 'fixe', fill=False)
    q = refl[k](*p)
    disc(ax, cx + q[0], cy + q[1], 1.3, 'varie')
text(ax, 44, 6, '4 + 4 = 8 éléments', 'encre', 'm')
save(fig, '74-070')
