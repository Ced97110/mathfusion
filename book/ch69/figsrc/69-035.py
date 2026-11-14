import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 21, 56, 'corps ordonné', 'sujet', 'm')
f = numberline(ax, 6, 34, 34, 0, 4, arrow_right=True)
for k in range(4):
    arrow(ax, (f(k) + 0.8, 38), (f(k + 1) - 0.8, 38), 'varie', curve=-0.5)
text(ax, 64, 62, 'cadran à 5 positions', 'limite', 's')
cx, cy, R = 64, 36, 16
pos = []
for k in range(5):
    a = math.radians(90 - 72 * k)
    pos.append((cx + R * math.cos(a), cy + R * math.sin(a)))
for k in range(5):
    p, q = pos[k], pos[(k + 1) % 5]
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + 5 * ux, p[1] + 5 * uy), (q[0] - 5 * ux, q[1] - 5 * uy), 'varie')
for k, (px, py) in enumerate(pos):
    disc(ax, px, py, 4.2, 'limite', label=str(k), size='s')
text(ax, cx, cy, r'$5\times 1=0$', 'limite', 's')
save(fig, '69-035')
