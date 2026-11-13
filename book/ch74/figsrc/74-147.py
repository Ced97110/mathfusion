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
fig, ax = canvas(84)
text(ax, 44, 79, r'frise $p2$ : bande de $N$', 'sujet', 'l')
for x in XS:
    gd(ax, 'N', x, 63, 9, 'sujet'); disc(ax, x, 63, 1.1, 'varie')
x0 = XS[0]
arc = [(x0 + 8 * math.cos(math.radians(t)), 63 + 8 * math.sin(math.radians(t))) for t in range(-30, 151, 10)]
line(ax, arc[:-1], 'varie', lw=0.9)
arrow(ax, arc[-2], arc[-1], 'varie')
text(ax, 44, 51, 'centres de demi-tour', 'varie', 'm')
text(ax, 44, 45, 'demi-tour : bande inchangée', 'resultat', 'm')
for x in XS:
    dline(ax, (x, 21), (x, 35)); gd(ax, 'N', x, 28, 9, 'fixe'); gd(ax, 'N', x, 28, 9, 'limite', fx=-1)
text(ax, 44, 38, 'miroir vertical', 'varie', 'm')
text(ax, 44, 13, r'$N$ inversé : bande changée', 'limite', 'm')
save(fig, '74-147')
