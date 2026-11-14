import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(62)
for cx, role in ((22, 'autre'), (66, 'sujet')):
    arc(ax, cx, 34, 14, 0, 2 * math.pi, 'fixe', 0.8)
for d in range(360):
    a = math.radians(d)
    r_ = 'autre' if a <= 2.0 else 'fixe'
    line(ax, [pol(22, 34, 14, a), pol(22, 34, 12.6, a)], r_, 0.25)
rad(ax, 22, 34, 14, 0, 'autre', 1.0); rad(ax, 22, 34, 14, 2.0, 'autre', 1.0)
arc(ax, 66, 34, 14, 0, 2.0, 'sujet', 2.2)
for a in (0, 1, 2):
    line(ax, [pol(66, 34, 12, a), pol(66, 34, 16, a)], 'varie', 1.3)
    q = pol(66, 34, 19.5, a)
    text(ax, q[0], q[1], f'{a}', 'varie', 's')
text(ax, 22, 56, 'degré', 'autre', 'l')
text(ax, 22, 13, 'on compte les parts', 'autre', 's')
text(ax, 22, 8, 'd’un tour de 360', 'autre', 's')
text(ax, 66, 56, 'radian', 'sujet', 'l')
text(ax, 66, 13, 'on pose une règle', 'sujet', 's')
text(ax, 66, 8, 'sur l’arc', 'sujet', 's')
save(fig, '29-046')
