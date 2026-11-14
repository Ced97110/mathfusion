import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
text(ax, 22, 58, 'G : 9 éléments', 'sujet', 'm')
for k in range(3):
    y = 14 + k*14
    box(ax, 4, y, 36, 11, 'sujet')
    for i in range(3):
        disc(ax, 12+i*10, y+5.5, 3.0, 'sujet')
text(ax, 22, 8, 'paquets de 3', 'sujet', 's')
arrow(ax, (42, 33), (50, 33), 'varie')
text(ax, 46, 38, r'$/C$', 'varie', 'm')
cx, cy, R = 68, 33, 11
ps = [(cx + R*math.cos(math.radians(90+120*i)), cy + R*math.sin(math.radians(90+120*i))) for i in range(3)]
for i in range(3):
    p, q = ps[i], ps[(i+1) % 3]
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy)
    arrow(ax, (p[0]+dx/d*5.5, p[1]+dy/d*5.5), (q[0]-dx/d*5.5, q[1]-dy/d*5.5), 'varie')
for p, l in zip(ps, [r'$C$', r'$aC$', r'$a^2C$']):
    disc(ax, p[0], p[1], 5, 'resultat', label=l, size='s')
text(ax, 68, 58, 'G/C : 3 éléments', 'resultat', 'm')
text(ax, 68, 8, r'$a$ les engendre tous', 'resultat', 's')
save(fig, '49-283')
