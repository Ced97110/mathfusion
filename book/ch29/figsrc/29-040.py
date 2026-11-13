import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(58)
cx, cy, R = 20, 30, 14
arc(ax, cx, cy, R, 0, 2.0, 'fixe', 0.8)
rad(ax, cx, cy, R, 0, 'sujet'); rad(ax, cx, cy, R, 2.0, 'sujet')
arc(ax, cx, cy, 5, 0, 2.0, 'sujet', 1.6)
p = pol(cx, cy, 9.5, 1.0)
text(ax, p[0], p[1], r'$\theta$', 'sujet', 'm')
text(ax, cx, 12, 'angle de 2 radians', 'sujet', 's')
arrow(ax, (36, 36), (45, 42), 'resultat')
arrow(ax, (36, 24), (45, 19), 'autre')
text(ax, 65, 52, 'écriture du livre', 'resultat', 's')
box(ax, 46, 38, 38, 10, 'resultat', label=r'$\theta=2$')
text(ax, 65, 28, 'autre écriture, avec unité', 'autre', 's')
box(ax, 46, 14, 38, 10, 'autre', label='2 rad')
save(fig, '29-040')
