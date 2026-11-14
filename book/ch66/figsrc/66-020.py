import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(70)
cx, cy, r = 40, 36, 24
disc(ax, cx, cy, r, 'fixe', fill=False)
for k in range(6):
    p = P(cx, cy, r, 60 * k)
    line(ax, [(cx, cy), p], 'fixe')
    disc(ax, p[0], p[1], 1.5, 'sujet')
    q = P(cx, cy, r + 6, 60 * k); text(ax, q[0], q[1], '%d°' % (60 * k), 'sujet', 's')
line(ax, [P(cx, cy, 9, 2 * i) for i in range(31)], 'varie')
q = P(cx, cy, 14, 30); text(ax, q[0], q[1], r'$2\pi/6$', 'varie', 's')
text(ax, 44, 5, r'6 points : 6 solutions de $z^6=1$', 'sujet', 's')
save(fig, '66-020')
