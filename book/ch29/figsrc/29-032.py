import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(62)
cx, cy, R = 22, 30, 15
arc(ax, cx, cy, R, 0, 2 * math.pi, 'fixe', 0.8)
arc(ax, cx, cy, R, 0, 2.0, 'varie', 2.2)
rad(ax, cx, cy, R, 0, 'sujet'); rad(ax, cx, cy, R, 2.0, 'sujet')
text(ax, cx + R / 2, cy - 2.4, r'$r$', 'sujet', 'm')
p = pol(cx, cy, R + 7, 1.0)
text(ax, p[0], p[1], r'arc $2r$', 'varie', 's')
text(ax, cx, cy - R - 4.5, 'angle : 2 radians', 'sujet', 's')
box(ax, 46, 40, 18, 7, 'sujet', label=r'$r$'); box(ax, 64, 40, 18, 7, 'sujet', label=r'$r$')
brace(ax, 46, 82, 40, 'varie', label=r'6 cm $=2r$')
text(ax, 64, 30, '6 cm : 2 radians', 'resultat', 's')
box(ax, 46, 14, 9, 7, 'sujet', label=r'$r/2$')
text(ax, 58, 17.5, '1,5 cm : 0,5 radian', 'resultat', 's', ha='left')
save(fig, '29-032')
