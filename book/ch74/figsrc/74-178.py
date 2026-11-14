import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, y0, d = 8, 22, 9
for i in range(3):
    for j in range(3): disc(ax, x0 + i*d, y0 + j*d, 2.2, 'autre')
arrow(ax, (x0 + 2.4, y0), (x0 + d - 2.4, y0), 'varie')
arrow(ax, (x0, y0 + 2.4), (x0, y0 + d - 2.4), 'varie')
text(ax, 17, 8, 'papier peint', 'autre', 's'); text(ax, 17, 52, '2 directions', 'autre', 's')
o = (62, 14); u = 8.5
for (i, j, k) in sorted(itertools.product(range(3), repeat=3), key=lambda c: (c[2] - c[0] - c[1], c[2])):
    p = iso(i, j, k, o, u); disc(ax, p[0], p[1], 2.3, 'sujet')
for v in ((1,0,0), (0,1,0), (0,0,1)):
    p = iso(0, 0, 0, o, u); q = iso(*v, o, u)
    dx, dy = q[0]-p[0], q[1]-p[1]; n = math.hypot(dx, dy); s = 2.6 / n
    arrow(ax, (p[0] + dx*s, p[1] + dy*s), (q[0] - dx*s, q[1] - dy*s), 'varie')
text(ax, 62, 52, '3 directions', 'sujet', 's'); text(ax, 62, 8, 'cristal', 'sujet', 's')
save(fig, '74-178')
