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

fig, ax = canvas(64)
ox, oy, sx, sy = 16, 10, 7.2, 0.95
arrow(ax, (ox, oy), (ox + 8 * sx + 6, oy), 'fixe'); arrow(ax, (ox, oy), (ox, oy + 45), 'fixe')
f = lambda x: 20 * math.sin(math.pi / 4 * (x - 2)) + 22
curve(ax, f, 0, 8, ox, oy, sx, sy, 'fixe', lw=1.0)
for xv, lab in ((1, '7,86'), (4, '42')):
    px, py = ox + xv * sx, oy + f(xv) * sy
    line(ax, [(px, oy), (px, py)], 'varie', dash=True); line(ax, [(ox, py), (px, py)], 'sujet', dash=True)
    disc(ax, px, py, 1.2, 'sujet')
    text(ax, px, oy - 3, str(xv), 'varie', 's'); text(ax, ox - 1.5, py, lab, 'sujet', 's', ha='right')
text(ax, ox + 4 * sx + 14, oy - 8, r'temps $x$ (min)', 'varie', 's')
text(ax, ox + 2, oy + 49, r'hauteur $y$ (m)', 'sujet', 's', ha='left')
text(ax, 62, 22, 'on choisit x,', 'varie', 's', ha='left'); text(ax, 62, 18, 'la formule donne y', 'sujet', 's', ha='left')
save(fig, '30-097')
