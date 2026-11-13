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
x0, w = 6, 9.5
brace(ax, x0, x0 + 8 * w, 40, 'sujet', label='un tour : 2π ≈ 6,283', down=False, size='m')
for i in range(8):
    box(ax, x0 + i * w, 22, w, 9, 'varie', label=str(i + 1), size='s')
text(ax, x0 + w / 2, 17.5, r'$B=\pi/4$', 'varie', 's', ha='left')
brace(ax, x0, x0 + 8 * w, 14, 'varie', label='8 pas = 8 minutes', down=True, size='s')
box(ax, 14, 1, 60, 0.01, 'fixe', fill=False) if False else None
text(ax, 44, 3, r'$2\pi \,/\, B = 8$ minutes', 'resultat', 'l')
save(fig, '30-099')
