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
oy, u = 33, 1.2
line(ax, [(4, oy), (84, oy)], 'fixe', dash=True)
for sg in (1, -1):
    y1 = oy + sg * u
    box(ax, 12, min(oy, y1), 8, abs(y1 - oy) if abs(y1 - oy) > 1.6 else 1.6, 'fixe')
    y2 = oy + sg * 20 * u
    box(ax, 60, min(oy, y2), 8, abs(y2 - oy), 'sujet')
text(ax, 25, oy + 3.5, '1', 'fixe', 's'); text(ax, 25, oy - 3.5, '−1', 'fixe', 's')
text(ax, 73, oy + 20 * u - 1, '20', 'sujet', 's', ha='left'); text(ax, 73, oy - 20 * u + 1, '−20', 'sujet', 's', ha='left')
text(ax, 16, 58, 'cercle', 'fixe', 'm'); text(ax, 64, 62, 'roue', 'sujet', 'm')
arrow(ax, (28, oy + 7), (56, oy + 7), 'varie'); text(ax, 42, oy + 11, r'$\times A$,  $A = 20$', 'varie', 's')
text(ax, 42, 4, 'hauteurs multipliées par 20', 'varie', 's')
save(fig, '30-101')
