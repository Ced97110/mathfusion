import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
GL = {
 'F': [[(-.35,-.5),(-.35,.5),(.4,.5)], [(-.35,.05),(.2,.05)]],
 'V': [[(-.5,.5),(0,-.5),(.5,.5)]],
 'D': [[(-.4,-.5),(-.4,.5),(0,.5),(.25,.4),(.4,.2),(.45,0),(.4,-.2),(.25,-.4),(0,-.5),(-.4,-.5)]],
 'N': [[(-.4,-.5),(-.4,.5),(.4,-.5),(.4,.5)]],
}
def gd(ax, k, cx, cy, s, role='sujet', fx=1, fy=1, ang=0, lw=1.2):
    c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    for st in GL[k]:
        pts = []
        for x, y in st:
            x, y = x * fx * s, y * fy * s
            pts.append((cx + x * c - y * sn, cy + x * sn + y * c))
        line(ax, pts, role, lw=lw)
def dline(ax, p, q, role='varie', lw=0.9):
    line(ax, [p, q], role, lw=lw, dash=True)
XS = [19 + 17 * i for i in range(4)]
fig, ax = canvas(64)
text(ax, 44, 59, r'$D_1$ : identité + 1 réflexion', 'sujet', 'm')
text(ax, 44, 52, '3 papiers, même groupe', 'encre', 'm')
for x0, kind, name, sub in [(6.5, 'pm', r'$pm$', 'miroir'), (34.5, 'pg', r'$pg$', 'symétrie glissée'), (62.5, 'cm', r'$cm$', 'maille centrée')]:
    for i in range(4):
        lx = x0 + 5.5 * i + 2.75
        line(ax, [(lx, 17), (lx, 45)], 'varie', dash=(kind == 'pg'))
    for i in range(5):
        for j in range(3):
            y = 36 - 8 * j + (4 if (kind == 'pg' and i % 2) else 0)
            mir = (i % 2 == 1) if kind in ('pm', 'pg') else ((i + j) % 2 == 1)
            gd(ax, 'F', x0 + 5.5 * i, y, 3.8, 'sujet', fx=-1 if mir else 1)
    text(ax, x0 + 11, 11, name, 'sujet', 'm'); text(ax, x0 + 11, 5, sub, 'varie', 's')
save(fig, '74-155')
