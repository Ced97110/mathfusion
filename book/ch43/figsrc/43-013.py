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

fig, ax = canvas(62)
box(ax, 2, 4, 84, 36, 'fixe', fill=False, dash=True)
spec = [(5, 22, 'sujet', 4), (30, 28, 'fixe', 5), (61, 22, 'fixe', 3)]
tgt = None
for x, w, role, n in spec:
    box(ax, x, 8, w, 28, role)
    pts = spots(x, 8, w, 28, n, cols=2 if n != 5 else 3)
    if role == 'sujet':
        pions(ax, pts[1:], role)
        disc(ax, pts[0][0], pts[0][1], 2.4, 'varie', label='$a$', size='s'); tgt = pts[0]
    else: pions(ax, pts, role)
text(ax, 12, 53, 'un point : $a$', 'varie', 'm')
text(ax, 44, 53, 'un bloc $A$ : 4 points', 'sujet', 'm')
text(ax, 77, 53, '$S$ : 12 points', 'fixe', 'm')
arrow(ax, (12, 50.5), (tgt[0] - 0.5, tgt[1] + 2.9), 'varie', lw=0.9)
arrow(ax, (40, 50.5), (22, 36.8), 'sujet', lw=0.9)
arrow(ax, (80, 50.5), (80, 41), 'fixe', lw=0.9)
save(fig, '43-013')
