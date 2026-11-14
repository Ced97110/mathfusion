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
fig, ax = canvas(60)
text(ax, 11, 54, 'point', 'encre', 's'); text(ax, 44, 54, 'mesure', 'sujet', 's'); text(ax, 77, 54, 'nombre', 'encre', 's')
box(ax, 29, 14, 30, 36, 'sujet')
text(ax, 44, 38, r'$5x^2$', 'sujet', 'm'); text(ax, 44, 32, r'$+\,6xy$', 'sujet', 'm'); text(ax, 44, 26, r'$+\,5y^2$', 'sujet', 'm')
for yy, p, r in ((40, r'$(1,\,1)$', '16'), (24, r'$(1,\,-1)$', '4')):
    box(ax, 2, yy - 5, 18, 10, 'fixe', label=p, size='s')
    arrow(ax, (21, yy), (28, yy), 'fixe')
    arrow(ax, (60, yy), (67, yy), 'resultat')
    box(ax, 68, yy - 5, 18, 10, 'resultat', label=r, size='l')
save(fig, '71-011')
