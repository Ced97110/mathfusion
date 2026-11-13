import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def pair(cx, cy, a, role, dash=False):
    L = 8
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    line(ax, [(cx - L, cy), (cx + L, cy)], role, lw=1.2, dash=dash)
    line(ax, [(cx - L * c, cy - L * s), (cx + L * c, cy + L * s)], role, lw=1.2, dash=dash)
xs = [12, 33, 54, 76]
for x, a, role, tx in zip(xs, [90, 45, 30, 36], ['resultat', 'resultat', 'resultat', 'limite'], ['90° : vu', '45° : vu', '30° : vu', '36° : jamais']):
    pair(x, 50, a, role, dash=(a == 36))
    text(ax, x, 34, tx, role, 's')
labs = ['36°', 'rotation 72°', 'ordre 5', 'interdit']
w = 18; gap = (W - 4 - 4 * w) / 3
for i, lb in enumerate(labs):
    x = 2 + i * (w + gap)
    box(ax, x, 8, w, 9, 'limite' if i == 3 else 'autre', label=lb, size='s')
    if i < 3: arrow(ax, (x + w, 12.5), (x + w + gap, 12.5), 'limite', lw=1.0)
save(fig, '74-114')
