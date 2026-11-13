import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(72)
P = lambda c, r, a: (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
for c, role, t1, t2, tq in [((20, 38), 'sujet', 'unité : le degré', 'tour = 360', 'quart = 90'), ((68, 38), 'autre', 'unité : 100 parts', 'tour = 100', 'quart = 25')]:
    R = 15
    pts = [c] + [P(c, R, 90 * i / 24) for i in range(25)]
    poly(ax, pts, 'varie')
    arc(ax, c, R, 0, 360, role, 1.1)
    text(ax, c[0], 61, t1, role, 's')
    text(ax, c[0], 16, t2, role, 'm')
    text(ax, c[0], 10, tq, 'varie', 'm')
text(ax, 44, 40, '=', 'fixe', 'l')
text(ax, 44, 33, 'même tour', 'fixe', 's')
save(fig, '25-005')
