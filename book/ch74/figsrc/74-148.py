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
fig, ax = canvas(110)
S = 5.5
text(ax, 44, 106, r'frise $p2mg$ : $V$ et $\Lambda$', 'sujet', 'm')
y1 = 96
for i, x in enumerate(XS):
    gd(ax, 'V', x, y1, S, 'sujet', fy=1 if i % 2 == 0 else -1); dline(ax, (x, y1 - 7.5), (x, y1 + 7.5))
for i in range(3): disc(ax, (XS[i] + XS[i + 1]) / 2, y1, 1.2, 'autre')
text(ax, 44, 83, 'miroirs verticaux', 'varie', 's')
text(ax, 44, 78, 'centres de demi-tour', 'autre', 's')
arrow(ax, (XS[0], 70), (XS[1], 70), 'varie')
text(ax, 42, 70, "glissement d'une lettre", 'varie', 's', ha='left')
for i, x in enumerate(XS): gd(ax, 'V', x, 62, S, 'limite', fy=-1 if i % 2 == 0 else 1)
text(ax, 44, 52, r'$V$ tombe sur $\Lambda$ : non', 'limite', 's')
text(ax, 44, 46, 'puis retourner haut-bas', 'varie', 's')
line(ax, [(7, 36), (81, 36)], 'varie', dash=True)
for i, x in enumerate(XS): gd(ax, 'V', x, 36, S, 'resultat', fy=1 if i % 2 == 0 else -1)
text(ax, 44, 25, 'symétrie glissée : oui', 'resultat', 's')
line(ax, [(7, 13), (81, 13)], 'varie', dash=True)
for i, x in enumerate(XS): gd(ax, 'V', x, 13, S, 'limite', fy=-1 if i % 2 == 0 else 1)
text(ax, 44, 3, 'retourner seul : non', 'limite', 's')
save(fig, '74-148')
