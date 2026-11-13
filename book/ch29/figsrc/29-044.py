import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(62)
text(ax, 44, 56, 'on tape : sin 30', 'encre', 'm')
box(ax, 6, 10, 34, 34, 'fixe')
box(ax, 10, 26, 26, 12, 'sujet', label='0,5', size='l')
text(ax, 23, 18, 'mode degrés', 'sujet', 's')
box(ax, 48, 10, 34, 34, 'fixe')
box(ax, 52, 26, 26, 12, 'autre', label='−0,988', size='l')
text(ax, 65, 18, 'mode radians', 'autre', 's')
arrow(ax, (34, 52), (23, 46), 'sujet')
arrow(ax, (54, 52), (65, 46), 'autre')
save(fig, '29-044')
