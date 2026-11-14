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
fig, ax = canvas(72)
text(ax, 26, 67, r'papier $p2$', 'sujet', 'l')
text(ax, 70, 67, r'groupe $C_2$', 'sujet', 'l')
for y in (54, 38):
    for cx in (14, 38):
        gd(ax, 'F', cx - 5, y, 8, 'sujet'); gd(ax, 'F', cx + 5, y, 8, 'sujet', fx=-1, fy=-1)
        disc(ax, cx, y, 1.1, 'varie')
text(ax, 26, 24, 'centres de demi-tour', 'varie', 'm')
line(ax, [(52, 12), (52, 62)], 'fixe', lw=0.6)
gd(ax, 'F', 62, 48, 8, 'sujet'); gd(ax, 'F', 79, 48, 8, 'resultat', fx=-1, fy=-1)
arrow(ax, (67, 48), (74, 48), 'varie')
text(ax, 70.5, 55, 'demi-tour', 'varie', 's')
text(ax, 62, 37, '0°', 'sujet', 'm'); text(ax, 79, 37, '180°', 'resultat', 'm')
text(ax, 70, 26, 'aucun miroir', 'fixe', 'm')
save(fig, '74-154')
