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
fig, ax = canvas(72)
cx, cy, k = 22, 54, 3.4
arrow(ax, (cx - 3.2 * k, cy), (cx + 3.2 * k, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - 11.5 * k), (cx, cy + 3 * k), 'fixe', lw=0.6)
ellipse1(ax, cx, cy, k, 'sujet')
for yy in (-3, -5, -7, -9):
    line(ax, [(cx - 3 * k, cy + yy * k), (cx + 3 * k, cy + yy * k)], 'fixe', dash=True, lw=0.6)
    text(ax, cx + 3 * k + 3, cy + yy * k, '?', 'fixe', 's')
line(ax, [(cx - 3 * k, cy - 10 * k), (cx + 3 * k, cy - 10 * k)], 'varie', dash=True)
text(ax, cx, cy - 10 * k - 3.5, r'$\times$', 'limite', 'l')
text(ax, 22, 68, 'première courbe', 'sujet', 's')
text(ax, 66, 54, 'elle semble bornée', 'sujet', 'm')
text(ax, 66, 47, 'à vérifier pour chaque y', 'varie', 's')
text(ax, 66, 22, r'$y=-10$ : aucun point', 'varie', 's')
text(ax, 66, 16, 'discriminant < 0', 'limite', 's')
save(fig, '71-006')
