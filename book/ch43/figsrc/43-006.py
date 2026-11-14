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

fig, ax = canvas(84)
xs = [30, 46, 62]
text(ax, 2, 78, '\u00e9l\u00e8ves', 'sujet', 'm', ha='left')
text(ax, 2, 62, 'chaises', 'autre', 'm', ha='left')
for x in xs:
    disc(ax, x, 78, 2.6, 'sujet')
    box(ax, x - 3, 59, 6, 6, 'autre')
    arrow(ax, (x, 75), (x, 66.5), 'fixe', lw=0.9)
line(ax, [(2, 52), (86, 52)], 'fixe', lw=0.5, dash=True)
text(ax, 2, 40, 'entiers', 'sujet', 'm', ha='left')
text(ax, 2, 16, 'pairs', 'autre', 'm', ha='left')
xs4 = [30, 44, 58, 72]
for i, x in enumerate(xs4):
    disc(ax, x, 40, 3, 'sujet', label=str(i), size='s')
    box(ax, x - 3.2, 12.8, 6.4, 6.4, 'autre', label=str(2 * i), size='s')
    arrow(ax, (x, 36.5), (x, 20.5), 'fixe', lw=0.9)
for k in range(3):
    disc(ax, 82 + k * 1.8, 40, 0.4, 'sujet'); disc(ax, 82 + k * 1.8, 16, 0.4, 'autre')
save(fig, '43-006')
