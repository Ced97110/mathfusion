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
fig, ax = canvas(98)
cx, cy = 44, 64
text(ax, 44, 94, r'$D_3$ : 3 rotations, 3 miroirs', 'sujet', 'l')
for deg in (90, 30, 150):
    t = math.radians(deg)
    line(ax, [(cx - 21 * math.cos(t), cy - 21 * math.sin(t)), (cx + 21 * math.cos(t), cy + 21 * math.sin(t))], 'varie', lw=0.8)
bx, by = 12 * math.cos(math.radians(72)), 12 * math.sin(math.radians(72))
for k in range(3):
    ang = 120 * k; c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    gd(ax, 'F', cx + bx * c - by * s, cy + bx * s + by * c, 5, 'sujet', ang=ang)
    mx, my = -bx, by
    gd(ax, 'F', cx + mx * c - my * s, cy + mx * s + my * c, 5, 'autre', fx=-1, ang=ang)
arrow(ax, (44, 41), (22, 29), 'fixe'); arrow(ax, (44, 41), (66, 29), 'fixe')
box(ax, 4, 14, 36, 14, 'resultat', label=r'$p3m1$', size='l')
box(ax, 48, 14, 36, 14, 'resultat', label=r'$p31m$', size='l')
text(ax, 44, 6, r'même $D_3$ : deux papiers', 'encre', 'm')
save(fig, '74-159')
