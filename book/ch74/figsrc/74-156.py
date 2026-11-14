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
fig, ax = canvas(70)
text(ax, 44, 65, r'$D_2$ : 4 éléments', 'sujet', 'l')
a, d, e = 18, 4, 4.5
x0, y0 = -d, e
for ox, kind, name, sub in [(11, 'pmm', r'$pmm$', 'deux miroirs'), (53, 'pmg', r'$pmg$', 'miroir + glissée')]:
    oy = 38
    if kind == 'pmm':
        els = [(x0, y0, 1, 1), (-x0, y0, -1, 1), (x0, -y0, 1, -1), (-x0, -y0, -1, -1)]
    else:
        els = [(x0, y0, 1, 1), (-x0, y0, -1, 1), (x0 + a / 2, -y0, 1, -1), (-x0 - a / 2, -y0, -1, -1)]
    for X in (0, 9, 18): line(ax, [(ox + X, oy - 8.5), (ox + X, oy + 8.5)], 'varie')
    line(ax, [(ox - 6, oy), (ox + 24, oy)], 'varie', dash=(kind == 'pmg'))
    for k in range(-1, 3):
        for (x, y, fx, fy) in els:
            X = x + a * k
            if -5.5 <= X <= 23.5: gd(ax, 'F', ox + X, oy + y, 4.2, 'sujet', fx=fx, fy=fy)
    text(ax, ox + 9, 19, name, 'sujet', 'm'); text(ax, ox + 9, 12, sub, 'varie', 's')
save(fig, '74-156')
