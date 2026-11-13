import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
import math
T = lambda p: (2 * p[0] + p[1], p[0] + 3 * p[1])
u = 2.6
def place(pts, cx, cy, u):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    mx, my = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    return [(cx + u * (x - mx), cy + u * (y - my)) for x, y in pts]
sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
rc = [(0, 0), (2, 0), (2, 3), (0, 3)]
n = 40
bl = [((1 + 0.22 * math.sin(3 * a) + 0.1 * math.cos(5 * a)) * 1.9 * math.cos(a), (1 + 0.22 * math.sin(3 * a) + 0.1 * math.cos(5 * a)) * 1.9 * math.sin(a)) for a in [i * 2 * math.pi / n for i in range(n)]]
shapes = [(sq, 1, 5, 11), (rc, 6, 30, 38), (bl, 12, 60, 69)]
for s, a, b, cx in shapes:
    poly(ax, place(s, cx, 82, u), 'sujet')
    arrow(ax, (cx, 71), (cx, 60), 'varie'); text(ax, cx + 1.5, 65.5, r'$\times 5$', 'varie', 's', ha='left')
    poly(ax, place([T(p) for p in s], cx, 33, u), 'resultat')
    text(ax, cx, 94, f'{a}' if a != 12 else '12', 'sujet', 'm'); text(ax, cx, 8, f'{b}', 'resultat', 'm')
save(fig, '76-005')
