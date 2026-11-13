import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(56)
cx, cy, R = 26, 28, 18
arc(ax, cx, cy, R, 0, 2 * math.pi, 'fixe', 0.8)
a1 = 1.5
arc(ax, cx, cy, R, 0, a1, 'varie', 2.4)
rad(ax, cx, cy, R, 0, 'fixe'); rad(ax, cx, cy, R, a1, 'fixe')
line(ax, [pol(cx, cy, R, 0), pol(cx, cy, R, a1)], 'limite', 1.0, dash=True)
p = pol(cx, cy, R + 4, 0.75)
text(ax, p[0], p[1], r'$s$', 'varie', 'l')
text(ax, cx + 4, cy - 8, 'corde : pas $s$', 'limite', 's')
text(ax, 66, 44, r'$s$', 'varie', 22)
text(ax, 66, 33, 'longueur de l’arc', 'varie', 's')
text(ax, 66, 28, 'le long de la courbe', 'varie', 's')
text(ax, 66, 18, r'$s=6$ ; $s=1{,}5$', 'encre', 's')
save(fig, '29-035')
