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
vals = ['0', '1', '2', '3', '4', '37']
for i, v in enumerate(vals):
    yy = 49 - i * 8.6
    box(ax, 2, yy - 3.5, 18, 7, 'varie', label=rf'$x = {v}$', size='s')
    arrow(ax, (20.5, yy), (32.5, 29 + (yy - 29) * 0.35), 'varie', lw=0.7)
box(ax, 33, 17, 36, 24, 'sujet')
text(ax, 51, 36, 'une seule formule', 'sujet', 's')
text(ax, 51, 28, r'$y = A\,\sin(B(x - C)) + D$', 'sujet', 's')
text(ax, 51, 21, r'$x$ : nombre au choix', 'varie', 's')
arrow(ax, (69.5, 29), (74.5, 29), 'sujet'); box(ax, 75, 25, 11, 8, 'resultat', label=r'$y$', size='m')
save(fig, '30-100')
