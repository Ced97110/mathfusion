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
ox, oy, sx, sy = 6, 24, 6.0, 12
arrow(ax, (ox, oy), (ox + 12 * sx + 4, oy), 'fixe', lw=0.7)
curve(ax, lambda x: math.sin(math.pi / 4 * x), 0, 12, ox, oy, sx, sy, 'sujet', lw=1.6)
curve(ax, lambda x: math.sin(math.pi / 4 * (x - 3)), 0, 12, ox, oy, sx, sy, 'autre', lw=1.6)
for xv in (2, 5):
    line(ax, [(ox + xv * sx, oy), (ox + xv * sx, oy + 15)], 'fixe', dash=True, lw=0.6)
    text(ax, ox + xv * sx, oy - 4, str(xv), 'fixe', 's')
arrow(ax, (ox + 2 * sx + 0.5, oy + 15), (ox + 5 * sx - 0.5, oy + 15), 'varie')
text(ax, ox + 3.5 * sx, oy + 19, 'déphasage : 3 min', 'varie', 's')
text(ax, 4, 5, 'roue 1', 'sujet', 'm', ha='left'); text(ax, 40, 5, 'roue 2, lancée 3 min après', 'autre', 's', ha='left')
save(fig, '30-106')
