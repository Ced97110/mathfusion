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

fig, ax = canvas(62)
oy = 33; sy = 0.55
for (ox, sg, px, role, lab, res) in ((6, 1, 8.5, 'sujet', r'$A = 20$', r'$|20| = 20$'), (50, -1, 25.5, 'autre', r'$A = -20$', r'$|-20| = 20$')):
    line(ax, [(ox, oy), (ox + 34, oy)], 'fixe', dash=True)
    curve(ax, lambda x: sg * 20 * math.sin(x), 0, 2 * math.pi, ox, oy, 34 / (2 * math.pi), sy, role, lw=1.4)
    arrow(ax, (ox + px, oy), (ox + px, oy + sg * 20 * sy), 'varie')
    text(ax, ox + px + 1.8, oy + sg * 6, '20', 'varie', 's', ha='left')
    text(ax, ox + 17, 56, lab, role, 'm')
    box(ax, ox + 3, 6, 28, 9, 'resultat', label=res, size='m')
    arrow(ax, (ox + 17, oy - 14), (ox + 17, 16.5), 'resultat')
text(ax, 44, 22, 'ligne médiane', 'fixe', 's')
save(fig, '30-098')
