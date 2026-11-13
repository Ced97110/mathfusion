import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(55)
cx, cy, R = 18, 22, 14
arc(ax, cx, cy, R, 0, 2.0, 'fixe', 0.8)
rad(ax, cx, cy, R, 0, 'fixe'); rad(ax, cx, cy, R, 2.0, 'fixe')
arc(ax, cx, cy, 5, 0, 2.0, 'sujet', 1.6)
p = pol(cx, cy, 9.5, 1.0)
text(ax, p[0], p[1], r'$\theta$', 'sujet', 'l')
arrow(ax, (35, 30), (47, 38), 'sujet')
text(ax, 67, 42, r'$\theta$', 'sujet', 26)
text(ax, 67, 30, 'angle au centre', 'sujet', 's')
text(ax, 67, 25, 'en radians', 'sujet', 's')
text(ax, 67, 15, r'$\theta=2$', 'resultat', 'l')
text(ax, 67, 8.5, 'arc 6 cm, rayon 3 cm', 'encre', 's')
save(fig, '29-034')
