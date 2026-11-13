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
text(ax, 26, 67, r'papier $p1$', 'sujet', 'l')
text(ax, 70, 67, r'groupe $C_1$', 'sujet', 'l')
for x in [9 + 11 * i for i in range(4)]:
    for y in (54, 42, 30): gd(ax, 'F', x, y, 7, 'sujet')
arrow(ax, (4, 20), (15, 20), 'varie'); arrow(ax, (4, 20), (4, 32), 'varie')
text(ax, 28, 11, 'translations seules', 'varie', 'm')
line(ax, [(52, 12), (52, 62)], 'fixe', lw=0.6)
gd(ax, 'F', 70, 48, 11, 'sujet', lw=1.5)
text(ax, 70, 34, 'seule rotation : 0°', 'sujet', 'm')
text(ax, 70, 27, 'aucun miroir', 'fixe', 'm')
save(fig, '74-153')
