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
fig, ax = canvas(58)
X, T, x0, y0 = 19, 7.5, 8, 16
poly(ax, [(x0, y0), (x0 + X, y0), (x0 + X, y0 + X), (x0, y0 + X)], 'sujet')
poly(ax, [(x0 + X, y0), (x0 + X + T, y0), (x0 + X + T, y0 + X), (x0 + X, y0 + X)], 'varie')
poly(ax, [(x0, y0 + X), (x0 + X, y0 + X), (x0 + X, y0 + X + T), (x0, y0 + X + T)], 'varie')
poly(ax, [(x0 + X, y0 + X), (x0 + X + T, y0 + X), (x0 + X + T, y0 + X + T), (x0 + X, y0 + X + T)], 'fixe')
text(ax, x0 + X / 2, y0 + X / 2, r'$x^2$', 'sujet', 'l')
text(ax, x0 + X + T / 2, y0 + X / 2, r'$3x$', 'varie', 's'); text(ax, x0 + X / 2, y0 + X + T / 2, r'$3x$', 'varie', 's')
text(ax, x0 + X + T / 2, y0 + X + T / 2, '9', 'fixe', 's')
text(ax, x0 + X / 2, y0 - 3, r'$x$', 'encre', 's'); text(ax, x0 + X + T / 2, y0 - 3, '3', 'encre', 's')
text(ax, x0 - 3, y0 + X / 2, r'$x$', 'encre', 's'); text(ax, x0 - 3, y0 + X + T / 2, '3', 'encre', 's')
text(ax, 67, 46, '9 : à retirer', 'fixe', 's'); arrow(ax, (50, 46), (x0 + X + T - 1, y0 + X + T - 1), 'fixe')
text(ax, 67, 29, 'deux bandes : 6x', 'varie', 's'); arrow(ax, (50, 29), (x0 + X + T - 1, y0 + X * 0.4), 'varie')
text(ax, 44, 5, r'$x^2+6x=(x+3)^2-9$', 'sujet', 'l')
save(fig, '71-010')
