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
text(ax, 44, 84, r'même groupe ponctuel $D_2$', 'sujet', 'm')
for ox, kind, name, sub in [(8, 'pgg', r'$pgg$', 'symétries glissées'), (56, 'cmm', r'$cmm$', 'miroirs, maille centrée')]:
    oy = 50
    if kind == 'pgg':
        els = [(4, 3, 1, 1), (-4, -3, -1, -1), (8, 15, -1, 1), (16, 9, 1, -1)]
        box(ax, ox, oy, 24, 24, 'fixe', fill=False, r=0.2, lw=0.5)
        for X in (6, 18): dline(ax, (ox + X, oy), (ox + X, oy + 24))
        for Y in (6, 18): dline(ax, (ox, oy + Y), (ox + 24, oy + Y))
    else:
        els = []
        for (x, y, fx, fy) in [(3.5, 3, 1, 1), (-3.5, 3, -1, 1), (3.5, -3, 1, -1), (-3.5, -3, -1, -1)]:
            els += [(x, y, fx, fy), (x + 12, y + 12, fx, fy)]
        for X in (0, 12, 24): line(ax, [(ox + X, oy), (ox + X, oy + 24)], 'varie')
        for Y in (0, 12, 24): line(ax, [(ox, oy + Y), (ox + 24, oy + Y)], 'varie')
    for (x, y, fx, fy) in els: gd(ax, 'F', ox + x % 24, oy + y % 24, 4.4, 'sujet', fx=fx, fy=fy)
    text(ax, ox + 12, 44, name, 'sujet', 'm'); text(ax, ox + 12, 38, sub, 'varie', 's')
for x, s, r in [(5, 'pmm', 'fixe'), (25, 'pmg', 'fixe'), (47, 'pgg', 'sujet'), (67, 'cmm', 'sujet')]:
    box(ax, x, 13, 17, 8, r, label=f'${s}$', size='m')
brace(ax, 5, 42, 22.5, 'fixe', 'ligne précédente : 2', down=False)
brace(ax, 47, 84, 22.5, 'sujet', 'cette ligne : 2', down=False)
text(ax, 44, 6, r'2 + 2 = 4 groupes pour $D_2$', 'resultat', 'm')
save(fig, '74-157')
