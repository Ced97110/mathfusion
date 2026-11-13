import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def hasse(ax, cx, y0, dx, dy, roles=None, hot=None, bw=7.5, bh=5.0, size='m'):
    roles = roles or {}; hot = hot or {}
    pos = {1: (cx, y0), 2: (cx - dx, y0 + dy), 3: (cx, y0 + dy), 5: (cx + dx, y0 + dy),
           6: (cx - dx, y0 + 2 * dy), 10: (cx, y0 + 2 * dy), 15: (cx + dx, y0 + 2 * dy), 30: (cx, y0 + 3 * dy)}
    edges = [(1, 2), (1, 3), (1, 5), (2, 6), (3, 6), (2, 10), (5, 10), (3, 15), (5, 15), (6, 30), (10, 30), (15, 30)]
    for a, b in edges:
        (xa, ya), (xb, yb) = pos[a], pos[b]
        line(ax, [(xa, ya + bh / 2), (xb, yb - bh / 2)], hot.get((a, b), 'fixe'), lw=1.6 if (a, b) in hot else 0.8)
    for n, (x, y) in pos.items():
        box(ax, x - bw / 2, y - bh / 2, bw, bh, roles.get(n, 'fixe'), label=str(n), size=size)
    return pos

def seg(ax, p, q, rp=0.0, rq=0.0, role='fixe', lw=0.8):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    line(ax, [(p[0] + ux * rp, p[1] + uy * rp), (q[0] - ux * rq, q[1] - uy * rq)], role, lw=lw)

def steps(ax, y_top, items, h=11, gap=4, nums=True):
    x0 = 12 if nums else 4
    cx = (x0 + 86) / 2; y = y_top
    for i, (role, l1, l2) in enumerate(items):
        yb = y - h
        box(ax, x0, yb, 86 - x0, h, role, lw=1.6 if role == 'varie' else 0.8)
        if l2:
            text(ax, cx, yb + h * 0.7, l1, role, 's'); text(ax, cx, yb + h * 0.27, l2, 'encre', 's')
        else:
            text(ax, cx, yb + h / 2, l1, role, 's')
        if nums: disc(ax, 7, yb + h / 2, 3, role, label=str(i + 1), size='s')
        if i < len(items) - 1: arrow(ax, (cx, yb), (cx, yb - gap), 'fixe')
        y = yb - gap

GX = {2: 40, 3: 53, 5: 66}
def grow(ax, y, name, present, role):
    text(ax, 30, y + 3.5, name, 'encre', 's', ha='right')
    for p, x in GX.items():
        if p in present: box(ax, x - 5.5, y, 11, 7, role, label=str(p), size='s')
        else: box(ax, x - 5.5, y, 11, 7, 'fixe', fill=False, dash=True, lw=0.5)

fig, ax = canvas(70)
leaves = [8 + i * 10.4 for i in range(8)]
yL, y2, y1, yr = 20, 34, 46, 57
l2 = [(leaves[2 * j] + leaves[2 * j + 1]) / 2 for j in range(4)]
l1 = [(l2[0] + l2[1]) / 2, (l2[2] + l2[3]) / 2]
root = ((l1[0] + l1[1]) / 2, yr)
for k in range(2):
    seg(ax, root, (l1[k], y1), 1.3, 3)
    for j in (2 * k, 2 * k + 1):
        seg(ax, (l1[k], y1), (l2[j], y2), 3, 1.3)
        for m in (2 * j, 2 * j + 1):
            seg(ax, (l2[j], y2), (leaves[m], yL + 3.5), 1.3, 0)
disc(ax, root[0], root[1], 1.3, 'fixe')
for k in range(2): disc(ax, l1[k], y1, 3, 'sujet', label=str(k), size='s')
for j in range(4): disc(ax, l2[j], y2, 1.3, 'fixe')
for m in range(8): box(ax, leaves[m] - 4.5, yL - 3.5, 9, 7, 'resultat', label=format(m, '03b'), size='s')
text(ax, 44, 65, 'chaque place : 0 ou 1', 'encre', 's')
text(ax, 44, 9, '2 × 2 × 2 = 8 listes', 'resultat', 'm')
save(fig, '80-221')
