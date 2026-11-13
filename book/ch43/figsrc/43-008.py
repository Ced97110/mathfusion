import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pos(cx, cy, R, h):
    a = math.radians(90 - 30 * h); return (cx + R * math.cos(a), cy + R * math.sin(a))
def clock(ax, cx, cy, R):
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
    for h in range(12):
        p = pos(cx, cy, R, h); disc(ax, p[0], p[1], 0.9, 'fixe')
def arcline(ax, cx, cy, r, h0, h1, role, lw=1.1):
    n = 24; pts = [pos(cx, cy, r, h0 + (h1 - h0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-3], pts[-1], role, lw=lw)
def spots(x, y, w, h, n, cols=3):
    rows = -(-n // cols); px = min(6.0, (w - 4) / max(cols - 1, 1)); py = min(7.0, (h - 6) / max(rows - 1, 1)) if rows > 1 else 0
    out = []
    for r in range(rows):
        cnt = min(cols, n - r * cols)
        for i in range(cnt):
            out.append((x + w / 2 + (i - (cnt - 1) / 2) * px, y + h / 2 + ((rows - 1) / 2 - r) * py))
    return out
def pions(ax, pts, role, r=1.6):
    for p in pts: disc(ax, p[0], p[1], r, role)
def pie(ax, cx, cy, r, n, k, role):
    for i in range(n):
        a0 = 90 - 360 * i / n; a1 = 90 - 360 * (i + 1) / n
        pts = [(cx, cy)] + [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * j / 6)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * j / 6))) for j in range(7)]
        if i < k: poly(ax, pts, role)
        else: poly(ax, pts, 'fixe', fill=False)

fig, ax = canvas(42)
x0 = 7.4; p = 6.2; gap = 2.5
groups = [(4, 'sujet'), (5, 'varie'), (3, 'autre')]
i = 0; c = []
for gi, (n, role) in enumerate(groups):
    xs = [x0 + (i + j) * p + gi * gap for j in range(n)]
    for x in xs: disc(ax, x, 21, 2.2, role)
    box(ax, xs[0] - 3.1, 14.5, xs[-1] - xs[0] + 6.2, 13, role, fill=False)
    text(ax, (xs[0] + xs[-1]) / 2, 33, str(n), role, 'xl', weight='bold')
    c.append(((xs[0] + xs[-1]) / 2, xs[-1] + 3.1, xs[0] - 3.1))
    i += n
text(ax, (c[0][0] + c[1][0]) / 2, 33, '+', 'encre', 'xl')
text(ax, (c[1][0] + c[2][0]) / 2, 33, '+', 'encre', 'xl')
brace(ax, c[0][2], c[2][1], 13, 'resultat', label='= 12 : tous les points de S')
save(fig, '43-008')
