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

fig, ax = canvas(60)
ox, oy, sx, sy = 8, 30, 68 / math.pi, 7
arrow(ax, (ox, oy), (ox + 72, oy), 'fixe', lw=0.7)
for a in (math.pi / 4, 3 * math.pi / 4):
    line(ax, [(ox + a * sx, oy - 20), (ox + a * sx, oy + 16)], 'fixe', dash=True, lw=0.6)
curve(ax, lambda x: math.tan(2 * x), 0, math.pi, ox, oy, sx, sy, 'sujet', n=600, lw=1.5, clip=2.6)
for xv in (math.pi / 8, 5 * math.pi / 8):
    disc(ax, ox + xv * sx, oy + sy, 1.2, 'varie')
arrow(ax, (ox + math.pi / 8 * sx + 1, oy + sy + 4), (ox + 5 * math.pi / 8 * sx - 1, oy + sy + 4), 'varie')
text(ax, ox + 3 * math.pi / 8 * sx, oy + 19, r'pas $\pi/2$ : $\tan = 1$', 'varie', 's')
text(ax, ox + math.pi / 8 * sx, oy - 4, 'π/8', 'varie', 's'); text(ax, ox + 5 * math.pi / 8 * sx, oy - 4, '5π/8', 'varie', 's')
text(ax, 84, 55, r'$\tan(2x)$', 'sujet', 'm', ha='right')
text(ax, 44, 4, r'période $\pi/B = \pi/2$', 'resultat', 'm')
save(fig, '30-111')
