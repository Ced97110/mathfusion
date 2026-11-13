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
fig, ax = canvas(88)
cx, cy = 44, 46
text(ax, 44, 83, '$p4$ : groupe ponctuel $C_4$', 'sujet', 'l')
n = 4
pts = []
for i in range(n):
    th = 90 + 360 / n * i
    px, py = cx + 15 * math.cos(math.radians(th)), cy + 15 * math.sin(math.radians(th))
    gd(ax, 'F', px, py, 8, 'sujet', ang=360 / n * i)
    text(ax, cx + 26 * math.cos(math.radians(th)), cy + 26 * math.sin(math.radians(th)), f'{round(360 / n * i)}°', 'varie', 'm')
    a0, a1 = math.radians(th + 25), math.radians(th + 360 / n - 25)
    arrow(ax, (cx + 7.5 * math.cos(a0), cy + 7.5 * math.sin(a0)), (cx + 7.5 * math.cos(a1), cy + 7.5 * math.sin(a1)), 'varie', curve=-0.3)
disc(ax, cx, cy, 1.3, 'varie')
text(ax, 44, 12, r'4 $\times$ 90° = 360°', 'resultat', 'm')
text(ax, 44, 6, 'aucun miroir', 'fixe', 'm')
save(fig, '74-160')
