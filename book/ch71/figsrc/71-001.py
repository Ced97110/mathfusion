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
fig, ax = canvas(62)
cx, cy, k = 25, 31, 14
plane(ax, cx, cy, k, 1.5)
text(ax, cx + 1.5 * k - 1, cy - 3, r'$x$', 'fixe', 's'); text(ax, cx + 2.5, cy + 1.5 * k - 1, r'$y$', 'fixe', 's')
ellipse1(ax, cx, cy, k, 'sujet')
disc(ax, cx + k, cy - k, 1.2, 'resultat', fill=True)
text(ax, cx + 9, cy - k - 4, r'$(1,\,-1)$', 'resultat', 's')
text(ax, cx - 9, cy + 13, 'courbe', 'sujet', 's')
text(ax, 69, 47, r'$x=1,\ y=-1$', 'sujet', 'm')
text(ax, 69, 36, r'$5-6+5=4$', 'resultat', 'l')
text(ax, 69, 25, '4 = 4 : le point est', 'resultat', 's')
text(ax, 69, 20, 'sur la courbe', 'resultat', 's')
save(fig, '71-001')
