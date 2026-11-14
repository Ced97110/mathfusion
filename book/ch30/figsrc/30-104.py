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

fig, ax = canvas(56)
ox, oy, sx, sy = 6, 22, 8.4, 0.6
f = lambda x: 20 * math.sin(math.pi / 4 * x)
line(ax, [(ox, oy), (ox + 68, oy)], 'fixe', lw=0.7)
line(ax, [(ox, oy + 22 * sy), (ox + 68, oy + 22 * sy)], 'sujet', dash=True, lw=0.7)
curve(ax, f, 0, 8, ox, oy, sx, sy, 'fixe')
curve(ax, lambda x: f(x) + 22, 0, 8, ox, oy, sx, sy, 'sujet', lw=1.6)
arrow(ax, (ox + 2 * sx, oy + 20 * sy), (ox + 2 * sx, oy + 42 * sy), 'varie')
text(ax, ox + 2 * sx + 2, oy + 31 * sy, r'$D = 22$', 'varie', 's', ha='left')
text(ax, ox + 72, oy, '0', 'fixe', 's', ha='left'); text(ax, ox + 72, oy + 22 * sy, '22', 'sujet', 's', ha='left')
text(ax, 4, 52, 'oscille autour de 0', 'fixe', 's', ha='left'); text(ax, 46, 52, 'oscille autour de 22', 'sujet', 's', ha='left')
text(ax, 44, 4, 'toute la courbe monte de D', 'varie', 's')
save(fig, '30-104')
