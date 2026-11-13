import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 5.5; y0 = 20
def tri(x0, pts_u, role, labels):
    pts = [(x0 + p[0] * u, y0 + p[1] * u) for p in pts_u]
    poly(ax, pts, role)
    cx = sum(p[0] for p in pts) / 3; cy = sum(p[1] for p in pts) / 3
    for i, lab in enumerate(labels):
        p, q = pts[i], pts[(i + 1) % 3]
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dx, dy = mx - cx, my - cy; n = math.hypot(dx, dy)
        text(ax, mx + dx / n * 2.6, my + dy / n * 2.6, lab, role, 's')
    return pts
r3 = math.sqrt(3)
tri(3, [(0, 0), (2, 0), (1, r3)], 'sujet', ['2', '2', '2'])
tri(20, [(0, 0), (4, 0), (4, 3)], 'fixe', ['4', '3', '5'])
tri(52, [(0, 0), (6, 0), (2.25, math.sqrt(16 - 2.25 ** 2))], 'fixe', ['6', '5', '4'])
text(ax, 8, 8, 'égaux', 'sujet', 'm')
text(ax, 31, 8, 'inégaux', 'limite', 'm')
text(ax, 68, 8, 'inégaux', 'limite', 'm')
save(fig, '25-087')
