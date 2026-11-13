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
text(ax, 44, 66, '5 + 5 = 10 groupes ponctuels', 'resultat', 'm')
def rosette(cx, cy, n, role, mir):
    if mir:
        for k in range(n):
            th = math.pi / 2 + math.pi * k / n
            line(ax, [(cx - 5 * math.cos(th), cy - 5 * math.sin(th)), (cx + 5 * math.cos(th), cy + 5 * math.sin(th))], 'fixe', lw=0.6)
    for k in range(n):
        th = math.pi / 2 + 2 * math.pi * k / n
        disc(ax, cx + 3.8 * math.cos(th), cy + 3.8 * math.sin(th), 0.8, role)
text(ax, 3, 59, r'$C_n$ : $n$ rotations', 'sujet', 's', ha='left')
text(ax, 3, 32, r'$D_n$ : $n$ rotations et $n$ miroirs', 'autre', 's', ha='left')
for letter, role, y0, mir in [('C', 'sujet', 36, False), ('D', 'autre', 9, True)]:
    for i, n in enumerate([1, 2, 3, 4, 6]):
        x = 3 + 16.9 * i
        box(ax, x, y0, 14.5, 19, role)
        text(ax, x + 7.25, y0 + 14.5, f'${letter}_{{{n}}}$', role, 'm')
        rosette(x + 7.25, y0 + 6.5, n, role, mir)
save(fig, '74-151')
