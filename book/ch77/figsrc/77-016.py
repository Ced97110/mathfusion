import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 14; O = (36, 12)
P = lambda x, y: (O[0] + x * u, O[1] + y * u)
th1 = math.atan2(1, 2); th2 = math.atan2(2, -1)
arrow(ax, P(-1.5, 0), P(2.4, 0), 'fixe', lw=0.6); arrow(ax, P(0, 0), P(0, 2.6), 'fixe', lw=0.6)
arrow(ax, P(0, 0), P(1, 0), 'sujet', lw=1.3); arrow(ax, P(0, 0), P(0, 1), 'sujet', lw=1.3)
arrow(ax, P(0, 0), P(2, 1), 'varie', lw=1.3); arrow(ax, P(0, 0), P(-1, 2), 'varie', lw=1.3)
for a0, a1 in ((0, th1), (math.pi / 2, th2)):
    line(ax, [(O[0] + 17 * math.cos(a0 + (a1 - a0) * t / 12), O[1] + 17 * math.sin(a0 + (a1 - a0) * t / 12)) for t in range(13)], 'varie')
def square(a, k):
    pts = [(0, 0), (k, 0), (k, k), (0, k)]
    c, s = math.cos(a), math.sin(a)
    q = [(O[0] + x * c - y * s, O[1] + x * s + y * c) for x, y in pts]
    line(ax, [q[1], q[2], q[3]], 'fixe')
square(0, 3); square(th1, 7)
text(ax, P(1, 0)[0], O[1] - 3.5, '1', 'sujet', 'm'); text(ax, O[0] + 3, P(0, 1)[1], r'$i$', 'sujet', 'm')
text(ax, P(2, 1)[0] + 7, P(2, 1)[1], r'$2+i$', 'varie', 'm')
text(ax, P(-1, 2)[0] - 3, P(-1, 2)[1] + 4, r'$-1+2i$', 'varie', 'm')
text(ax, O[0] + 20.5 * math.cos(th1 / 2), O[1] + 20.5 * math.sin(th1 / 2) + 1, r'$\theta$', 'varie', 'm')
a = (math.pi / 2 + th2) / 2
text(ax, O[0] + 20.5 * math.cos(a), O[1] + 20.5 * math.sin(a), r'$\theta$', 'varie', 'm')
text(ax, 44, 3, r'quart de tour : $(2\,;1)\to(-1\,;2)$', 'fixe', 's', ha='center')
save(fig, '77-016')
