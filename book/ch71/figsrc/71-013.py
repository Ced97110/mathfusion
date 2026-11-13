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
k = 5; x0, y0 = 24, 22
A = (x0, y0); B = (x0 + 3 * k, y0); C = (x0 + 3 * k, y0 + 4 * k); n = (-4 * k, 3 * k)
poly(ax, [(A[0], A[1] - 3 * k), (B[0], B[1] - 3 * k), B, A], 'sujet')
poly(ax, [B, (B[0] + 4 * k, B[1]), (C[0] + 4 * k, C[1]), C], 'sujet')
poly(ax, [A, C, (C[0] + n[0], C[1] + n[1]), (A[0] + n[0], A[1] + n[1])], 'resultat')
poly(ax, [A, B, C], 'fixe')
arrow(ax, A, C, 'varie', lw=1.3)
text(ax, x0 + 1.5 * k, y0 - 1.5 * k, r'$3^2=9$', 'sujet', 's')
text(ax, B[0] + 2 * k, y0 + 2 * k, r'$4^2=16$', 'sujet', 's')
text(ax, A[0] + 0.5 * (C[0] - A[0]) + n[0] / 2, A[1] + 0.5 * (C[1] - A[1]) + n[1] / 2, r'$5^2=25$', 'resultat', 's')
text(ax, 71, 52, 'flèche : 3 et 4', 'varie', 's')
text(ax, 71, 36, r'$9+16=25$', 'resultat', 'l')
text(ax, 71, 29, 'longueur au carré', 'resultat', 's')
save(fig, '71-013')
