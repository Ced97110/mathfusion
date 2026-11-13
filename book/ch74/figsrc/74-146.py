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
text(ax, 44, 79, r'frise $p11m$ : bande de $D$', 'sujet', 'l')
line(ax, [(8, 62), (80, 62)], 'varie', dash=True)
for x in XS: gd(ax, 'D', x, 62, 9, 'sujet')
text(ax, 44, 47, 'miroir horizontal : oui', 'varie', 'm')
for x in XS:
    dline(ax, (x, 19), (x, 33)); gd(ax, 'D', x, 26, 9, 'fixe'); gd(ax, 'D', x, 26, 9, 'limite', fx=-1)
text(ax, 44, 38, 'miroir vertical : non', 'varie', 'm')
text(ax, 44, 12, r'$D$ inversé : bande changée', 'limite', 'm')
save(fig, '74-146')
