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

fig, ax = canvas(66)
ox, oy, sx, sy = 16, 6, 6.8, 1.15
f = lambda x: 20 * math.sin(math.pi / 4 * (x - 2)) + 22
for v in (42, 2):
    line(ax, [(ox, oy + v * sy), (ox + 8 * sx, oy + v * sy)], 'fixe', dash=True, lw=0.7)
    text(ax, ox - 2, oy + v * sy, str(v), 'fixe', 's', ha='right')
curve(ax, f, 0, 8, ox, oy, sx, sy, 'fixe', lw=1.2)
line(ax, [(ox, oy + 22 * sy), (ox + 8 * sx + 2, oy + 22 * sy)], 'sujet', lw=1.8)
text(ax, ox - 2, oy + 22 * sy, '22', 'sujet', 's', ha='right')
arrow(ax, (ox + 5 * sx, oy + 22 * sy), (ox + 5 * sx, oy + 42 * sy), 'varie'); text(ax, ox + 5 * sx + 1.5, oy + 32 * sy, '20', 'varie', 's', ha='left')
arrow(ax, (ox + 1 * sx, oy + 22 * sy), (ox + 1 * sx, oy + 2 * sy), 'varie'); text(ax, ox + 1 * sx + 1.5, oy + 12 * sy, '20', 'varie', 's', ha='left')
text(ax, ox + 8 * sx + 3, oy + 22 * sy + 4, r'$y = D$', 'sujet', 'm', ha='left')
text(ax, ox + 8 * sx + 3, oy + 22 * sy - 4, 'milieu', 'sujet', 's', ha='left')
text(ax, 44, 2, 'hauteurs en mètres', 'fixe', 's')
save(fig, '30-105')
