import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
S2 = math.sqrt(2)
def plane(ax, cx, cy, k, ex=3, ey=None, x0=None, y0=None):
    ey = ey or ex; x0 = -ex if x0 is None else x0; y0 = -ey if y0 is None else y0
    arrow(ax, (cx + x0 * k, cy), (cx + ex * k, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy + y0 * k), (cx, cy + ey * k), 'fixe', lw=0.6)
def clipline(ax, cx, cy, k, pts, role, x0, x1, y0, y1):
    seg = []
    for x, y in pts:
        if x0 <= x <= x1 and y0 <= y <= y1: seg.append((cx + x * k, cy + y * k))
        else:
            if len(seg) > 1: line(ax, seg, role, lw=1.1)
            seg = []
    if len(seg) > 1: line(ax, seg, role, lw=1.1)
def ellipse1(ax, cx, cy, k, role):
    t = np.linspace(0, 2 * math.pi, 240)
    line(ax, [(cx + (math.sqrt(.5) * math.cos(q) + S2 * math.sin(q)) / S2 * k, cy + (math.sqrt(.5) * math.cos(q) - S2 * math.sin(q)) / S2 * k) for q in t], role, lw=1.1)
def hyper2(ax, cx, cy, k, role, x0, x1, y0, y1):
    a = math.sqrt(4 / 3); b = 2
    for s in (1, -1):
        pts = [((s * a * math.cosh(q) + b * math.sinh(q)) / S2, (s * a * math.cosh(q) - b * math.sinh(q)) / S2) for q in np.linspace(-6, 6, 3000)]
        clipline(ax, cx, cy, k, pts, role, x0, x1, y0, y1)
fig, ax = canvas(70)
text(ax, 44, 65, 'sans terme croisé', 'fixe', 'm')
box(ax, 14, 47, 24, 12, 'fixe', label=r'$x^2$', size='l'); text(ax, 44, 53, '+', 'encre', 'l'); box(ax, 50, 47, 24, 12, 'fixe', label=r'$y^2$', size='l')
text(ax, 26, 42, 'x seul', 'fixe', 's'); text(ax, 62, 42, 'y seul', 'fixe', 's')
text(ax, 44, 32, 'avec terme croisé', 'sujet', 'm')
box(ax, 3, 14, 24, 12, 'fixe', label=r'$5x^2$', size='l'); text(ax, 31, 20, '+', 'encre', 'l')
box(ax, 34, 14, 20, 12, 'sujet', label=r'$6xy$', size='l', weight='bold'); text(ax, 58, 20, '+', 'encre', 'l')
box(ax, 61, 14, 24, 12, 'fixe', label=r'$5y^2$', size='l')
text(ax, 44, 8, 'x et y mélangés', 'sujet', 's')
save(fig, '71-007')
