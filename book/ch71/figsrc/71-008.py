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
fig, ax = canvas(64)
k = 8
plane(ax, 22, 36, k, 2.2); plane(ax, 66, 36, k, 2.2)
t = np.linspace(0, 2 * math.pi, 200)
line(ax, [(22 + k * math.cos(q), 36 + k * math.sin(q)) for q in t], 'sujet', lw=1.2)
tt = np.linspace(-1.5, 1.5, 200)
for s in (1, -1):
    line(ax, [(66 + s * k * math.cosh(q), 36 + k * math.sinh(q)) for q in tt if math.cosh(q) <= 2.15], 'autre', lw=1.2)
text(ax, 22, 59, r'$x^2+y^2=1$', 'sujet', 'm'); text(ax, 66, 59, r'$x^2-y^2=1$', 'autre', 'm')
text(ax, 22, 12, 'plus : courbe fermée', 'sujet', 's')
text(ax, 66, 12, 'moins : ouverte,', 'autre', 's'); text(ax, 66, 7, 'deux morceaux', 'autre', 's')
save(fig, '71-008')
