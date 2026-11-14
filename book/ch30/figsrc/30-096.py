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

fig, ax = canvas(84)
box(ax, 2, 70, 84, 12, 'sujet', label=r'Prémisses : $A \neq 0$ et $B > 0$', size='m')
arrow(ax, (44, 69), (44, 62), 'fixe')
ox, oy, sx, sy = 6, 38, 50 / (2 * math.pi), 6
line(ax, [(ox, oy), (ox + 52, oy)], 'fixe')
curve(ax, lambda x: math.sin(x), 0, 2 * math.pi, ox, oy, sx, sy, 'fixe')
curve(ax, lambda x: 3 * math.sin(2 * x), 0, 2 * math.pi, ox, oy, sx, sy, 'sujet', lw=1.5)
xs = math.pi / 4
arrow(ax, (ox + xs * sx, oy + math.sin(xs) * sy), (ox + xs * sx, oy + 3 * sy), 'varie')
text(ax, 60, oy + 20, r'$\sin x$', 'fixe', 's', ha='left')
text(ax, 60, oy + 14, r'$3\,\sin(2x)$', 'sujet', 's', ha='left')
text(ax, 60, oy + 6, 'étirement |A|', 'varie', 's', ha='left')
text(ax, 60, oy - 2, 'resserrement B', 'varie', 's', ha='left')
text(ax, 60, oy - 12, 'décalage C, D', 'varie', 's', ha='left')
arrow(ax, (8, 12), (30, 12), 'varie'); text(ax, 19, 6, r'$C$ à droite', 'varie', 's')
arrow(ax, (50, 5), (50, 19), 'varie'); text(ax, 68, 12, r'$D$ en haut', 'varie', 's')
save(fig, '30-096')
