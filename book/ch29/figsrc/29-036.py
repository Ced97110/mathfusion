import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9):
    line(ax, [(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(55)
cx, cy, R = 22, 28, 15
a0, a1 = 0.1, 1.2
arc(ax, cx, cy, R, 0, 2 * math.pi, 'fixe', 0.8)
rad(ax, cx, cy, R, a0, 'fixe', 1.0)
rad(ax, cx, cy, R, a1, 'sujet', 2.4)
arc(ax, cx, cy, R, a0, a1, 'varie', 2.4)
p = pol(cx, cy, 8, a1)
text(ax, p[0] - 3, p[1] + 1, r'$r$', 'sujet', 'l')
q = pol(cx, cy, R + 3.8, (a0 + a1) / 2)
text(ax, q[0], q[1], r'$s$', 'varie', 'l')
q = pol(cx, cy, 7, (a0 + a1) / 2)
text(ax, q[0], q[1], r'$\theta$', 'fixe', 'm')
text(ax, cx, cy - R - 4.5, 'rayon : 3 cm', 'sujet', 's')
text(ax, 54, 30, r'$\theta=$', 'encre', 'l')
line(ax, [(60, 30), (80, 30)], 'encre', 1.0)
text(ax, 70, 36, r'$s$', 'varie', 'l')
box(ax, 65, 22, 10, 6, 'sujet', label=r'$r$')
text(ax, 70, 15, 'sous la barre', 'sujet', 's')
save(fig, '29-036')
