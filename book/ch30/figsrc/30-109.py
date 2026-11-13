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
text(ax, 22, 51, 'hertz', 'sujet', 'm'); text(ax, 68, 51, 'cycles par minute', 'fixe', 's')
box(ax, 2, 31, 40, 11, 'sujet', label='440 hertz', size='m')
box(ax, 50, 31, 36, 11, 'fixe', label='26 400 par min', size='m')
arrow(ax, (42.5, 36.5), (49.5, 36.5), 'varie'); text(ax, 46, 41, '× 60', 'varie', 's')
box(ax, 2, 10, 40, 11, 'sujet', label='≈ 0,002 hertz', size='m')
box(ax, 50, 10, 36, 11, 'fixe', label='0,125 par min', size='m')
arrow(ax, (49.5, 15.5), (42.5, 15.5), 'varie'); text(ax, 46, 20, '÷ 60', 'varie', 's')
text(ax, 22, 5, 'roue', 'encre', 's'); text(ax, 22, 46, 'guitare', 'encre', 's')
save(fig, '30-109')
