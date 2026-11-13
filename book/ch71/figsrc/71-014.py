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
k, x0, y0 = 9, 5, 12
for i in range(6): line(ax, [(x0 + i * k, y0), (x0 + i * k, y0 + 4 * k)], 'fixe', lw=0.4)
for j in range(5): line(ax, [(x0, y0 + j * k), (x0 + 5 * k, y0 + j * k)], 'fixe', lw=0.4)
P = lambda x, y: (x0 + x * k, y0 + y * k)
poly(ax, [P(0, 0), P(3, 1), P(4, 3), P(1, 2)], 'sujet')
arrow(ax, P(0, 0), P(3, 1), 'varie', lw=1.4); arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.4)
text(ax, 69, 50, 'flèche 1 : 3 et 1', 'varie', 's'); text(ax, 69, 43, 'flèche 2 : 1 et 2', 'autre', 's')
text(ax, 69, 30, 'parallélogramme', 'sujet', 's')
text(ax, 69, 22, 'aire : 5 carreaux', 'resultat', 'm')
save(fig, '71-014')
