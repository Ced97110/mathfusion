import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$G$ agit sur lui-même', 'sujet', 'm')
cx, cy, R = 44, 36, 20
names = ['1', r'$r$', r'$r^2$', r'$r^3$']
pos = [(cx, cy - R), (cx + R, cy), (cx, cy + R), (cx - R, cy)]
for i in range(4):
    p, q = pos[i], pos[(i + 1) % 4]
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + 5.2 * ux, p[1] + 5.2 * uy), (q[0] - 5.2 * ux, q[1] - 5.2 * uy), 'varie', curve=0.0)
for n, (x, y) in zip(names, pos):
    disc(ax, x, y, 4.4, 'sujet', label=n, size='m')
text(ax, cx, cy, r'$r\times$', 'varie', 'm')
text(ax, 44, 7, r'$r \times r^2 = r^3$ et $r \times 1 = r$', 'encre', 's')
save(fig, '49-114')
