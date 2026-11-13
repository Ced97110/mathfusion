import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
F = [[(-.35, -.5), (-.35, .5), (.4, .5)], [(-.35, .05), (.2, .05)]]
def gd(cx, cy, s, role, fx=1, fy=1, ang=0, lw=1.6):
    c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    for st in F:
        pts = []
        for x, y in st:
            x, y = x * fx * s, y * fy * s
            pts.append((cx + x * c - y * sn, cy + x * sn + y * c))
        line(ax, pts, role, lw=lw)
fig, ax = canvas(84)
text(ax, 44, 79, 'frise : direction horizontale', 'sujet', 's')
for k in range(6): gd(14 + k * 12, 68, 7, 'sujet')
arrow(ax, (8, 58), (80, 58), 'sujet', both=True, lw=0.9)
# four kept linear parts
text(ax, 31, 51, 'direction horizontale gardée', 'resultat', 's')
names = [('I', 1, 1, 0), (r'$-I$', 1, 1, 180), ('réflexion', 1, -1, 0), ('réflexion', -1, 1, 0)]
for i, (n, fx, fy, a) in enumerate(names):
    x = 3 + i * 14.5
    box(ax, x, 20, 13, 26, 'resultat')
    gd(x + 6.5, 35, 7, 'resultat', fx, fy, a)
    text(ax, x + 6.5, 25, n, 'resultat', 's')
brace(ax, 3, 59.5, 18, 'resultat', r'groupe $D_2$')
# quarter turn
box(ax, 64, 20, 21, 26, 'limite')
gd(74.5, 35, 7, 'limite', ang=90)
text(ax, 74.5, 25, 'quart de tour', 'limite', 's')
text(ax, 74.5, 51, 'verticale : non', 'limite', 's')
save(fig, '74-143')
