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
        pts = [(cx, cy)] + [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * j / max(6, 48 // n))), cy + r * math.sin(math.radians(a0 + (a1 - a0) * j / max(6, 48 // n)))) for j in range(max(6, 48 // n) + 1)]
        if i < k: poly(ax, pts, role)
        else: poly(ax, pts, 'fixe', fill=False)

fig, ax = canvas(80)
cfg = [(15, 4, 3, r'$\frac{3}{4}$'), (44, 8, 6, r'$\frac{6}{8}$'), (73, 12, 9, r'$\frac{9}{12}$')]
for cx, n, k, s in cfg:
    pie(ax, cx, 66, 10, n, k, 'sujet')
    text(ax, cx, 48, s, 'sujet', 'l')
    arrow(ax, (cx, 44), (cx, 31), 'sujet', lw=0.8)
box(ax, 3, 6, 82, 25, 'resultat')
text(ax, 44, 23, r'$\left\{\frac{3}{4},\ \frac{6}{8},\ \frac{9}{12},\ \ldots\right\}$', 'encre', 'l')
text(ax, 44, 10.5, 'le nombre trois quarts', 'resultat', 'm')
save(fig, '43-005')
