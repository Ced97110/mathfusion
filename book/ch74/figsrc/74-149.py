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
fig, ax = canvas(66)
text(ax, 22, 60, 'papiers peints', 'sujet', 'l')
text(ax, 66, 60, 'frises', 'autre', 'l')
box(ax, 3, 30, 38, 22, 'resultat')
text(ax, 22, 46, 'preuve donnée', 'resultat', 'm')
text(ax, 22, 37, 'ordres 1, 2, 3, 4 ou 6', 'resultat', 's')
for i in range(7): box(ax, 48 + 5.2 * i, 41, 4.4, 4.4, 'autre', dash=True, r=0.4)
text(ax, 66, 35, '7 groupes : admis', 'autre', 'm')
text(ax, 66, 29, 'preuve non vue ici', 'autre', 's')
arrow(ax, (41.5, 41), (47, 43), 'varie')
text(ax, 44, 20, 'même genre de preuve', 'varie', 'm')
save(fig, '74-149')
