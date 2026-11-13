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
fig, ax = canvas(80)
for i in range(10): box(ax, 4 + 5.4 * (i % 5), 66 - 5.4 * (i // 5), 4.4, 4.4, 'sujet', r=0.4)
for i in range(17): box(ax, 52 + 5.4 * (i % 6), 68.7 - 5.4 * (i // 6), 4.4, 4.4, 'resultat', r=0.4)
arrow(ax, (33, 64), (48, 64), 'varie')
text(ax, 40.5, 69, 'tout essayer', 'varie', 's')
text(ax, 17, 50, '10 groupes ponctuels', 'sujet', 's')
text(ax, 68, 50, '17 groupes', 'resultat', 'm')
for y, s in [(34, 'pour chaque groupe ponctuel'), (22, 'chaque type de réseau'), (10, 'miroir, glissée ou les deux')]:
    box(ax, 3, y, 44, 8, 'varie', label=s, size='s')
arrow(ax, (25, 34), (25, 30.5), 'fixe'); arrow(ax, (25, 22), (25, 18.5), 'fixe')
box(ax, 52, 16, 33, 18, 'resultat')
text(ax, 68.5, 28, 'plus rien', 'resultat', 'm'); text(ax, 68.5, 21, 'à essayer', 'resultat', 'm')
arrow(ax, (47.5, 14), (51.5, 19), 'resultat')
save(fig, '74-150')
