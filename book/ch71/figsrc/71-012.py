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
fig, ax = canvas(56)
text(ax, 44, 51, 'deux paniers différents', 'encre', 'm')
text(ax, 21, 43, 'panier 1', 'encre', 's'); text(ax, 61, 43, 'panier 2', 'encre', 's')
w = 11
def row(x, items):
    for i, r in enumerate(items):
        box(ax, x + i * (w + 1), 28, w, 10, 'sujet' if r == 0 else 'autre', label='pomme' if r == 0 else 'poire', size='s')
row(3, [0, 1, 1]); row(50, [0, 0])
text(ax, 21, 21, r'$2\times1+2=4$', 'resultat', 'm'); text(ax, 61, 21, r'$2\times2+0=4$', 'resultat', 'm')
box(ax, 20, 4, 48, 10, 'resultat', label='même prix : 4 €', size='m')
save(fig, '71-012')
