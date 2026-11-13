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
text(ax, 24, 57, 'période', 'fixe', 'm'); text(ax, 66, 57, 'fréquence', 'sujet', 'm')
rows = ((44, 'guitare', '1/440 s', '440 par s'), (24, 'roue', '8 min', '0,125 par min'))
for y, nom, per, fr in rows:
    box(ax, 4, y - 5, 40, 10, 'fixe', label=per, size='m')
    box(ax, 52, y - 5, 34, 10, 'sujet', label=fr, size='m')
    arrow(ax, (44.5, y), (51.5, y), 'varie', both=True)
    text(ax, 48, y + 6.5, nom, 'encre', 's')
text(ax, 44, 8, r'$f = 1/\mathrm{période} = B/2\pi$', 'resultat', 'm')
save(fig, '30-108')
