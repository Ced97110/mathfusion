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
ox, sx = 8, 66 / (2 * math.pi)
for oy, f, role, lab in ((50, lambda x: math.sin(x), 'fixe', r'$B = 1$ : un cycle en $2\pi$'), (22, lambda x: math.sin(2 * x), 'sujet', r'$B = 2$ : un cycle en $\pi$')):
    line(ax, [(ox, oy), (ox + 68, oy)], 'fixe', lw=0.6)
    curve(ax, f, 0, 2 * math.pi, ox, oy, sx, 7, role, lw=1.4)
    text(ax, ox, oy + 11, lab, role, 's', ha='left')
for xv, lab in ((0, '0'), (math.pi, 'π'), (2 * math.pi, '2π')):
    line(ax, [(ox + xv * sx, 12), (ox + xv * sx, 51)], 'fixe', dash=True, lw=0.5)
    text(ax, ox + xv * sx, 6, lab, 'fixe', 's')
arrow(ax, (ox, 13.5), (ox + math.pi * sx, 13.5), 'varie', both=True)
text(ax, ox + math.pi * sx / 2, 17.5, r'$x$ avance de $\pi$', 'varie', 's')
save(fig, '30-102')
