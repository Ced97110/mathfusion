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

fig, ax = canvas(58)
ox, oy, sx, sy = 8, 26, 8.4, 14
arrow(ax, (ox, oy), (ox + 8 * sx + 6, oy), 'fixe', lw=0.7)
curve(ax, lambda x: math.sin(math.pi / 4 * x), 0, 8, ox, oy, sx, sy, 'fixe', lw=1.2)
curve(ax, lambda x: math.sin(math.pi / 4 * (x - 2)), 0, 8, ox, oy, sx, sy, 'sujet', lw=1.6)
disc(ax, ox, oy, 1.2, 'fixe'); disc(ax, ox + 2 * sx, oy, 1.2, 'sujet')
arrow(ax, (ox + 0.6, oy + 5), (ox + 2 * sx - 0.6, oy + 5), 'varie')
text(ax, ox + sx, oy + 9, r'$C = 2$', 'varie', 's')
text(ax, ox, oy - 4, '0', 'fixe', 's'); text(ax, ox + 2 * sx, oy - 4, '2', 'sujet', 's')
text(ax, 4, 53, 'sinus de départ', 'fixe', 's', ha='left')
text(ax, 44, 53, 'même courbe, 2 min plus loin', 'sujet', 's', ha='left')
text(ax, 44, 5, r'montée par 0 : $x = C$', 'sujet', 's')
save(fig, '30-103')
