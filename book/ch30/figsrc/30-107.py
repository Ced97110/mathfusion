import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def curve(ax, f, a, b, ox, oy, sx, sy, role, n=160, lw=1.2, clip=None, dash=False):
    seg = []
    for i in range(n + 1):
        x = a + (b - a) * i / n; y = f(x)
        if clip is not None and abs(y) > clip:
            if len(seg) > 1: line(ax, seg, role, lw=lw, dash=dash)
            seg = []; continue
        seg.append((ox + x * sx, oy + y * sy))
    if len(seg) > 1: line(ax, seg, role, lw=lw, dash=dash)

fig, ax = canvas(72)
ox, oy, sx, sy = 4, 6, 5.0, 1.3
f = lambda x: 20 * math.sin(math.pi / 4 * (x - 2)) + 22
curve(ax, f, 0, 8, ox, oy, sx, sy, 'fixe', lw=1.0)
rows = ((42, 'fixe', 'haut : y = D + |A| = 42'), (22, 'sujet', 'médiane : y = D = 22'),
        (2, 'fixe', 'bas : y = D − |A| = 2'), (0, 'autre', 'sol : y = 0'))
for v, role, lab in rows:
    line(ax, [(ox, oy + v * sy), (ox + 8 * sx + 4, oy + v * sy)], role, lw=1.8 if role == 'sujet' else 0.9, dash=(role == 'fixe'))
    text(ax, ox + 8 * sx + 6, oy + v * sy, lab, role, 's', ha='left')
text(ax, 44, 68, 'quatre droites horizontales', 'encre', 's')
save(fig, '30-107')
