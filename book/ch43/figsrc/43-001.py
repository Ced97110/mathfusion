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
cx, cy, R = 24, 31, 17
clock(ax, cx, cy, R)
for h, s in [(0, '12'), (3, '3'), (6, '6'), (9, '9')]:
    p = pos(cx, cy, R + 4.2, h); text(ax, p[0], p[1], s, 'sujet' if h == 9 else 'fixe', 'm')
p9 = pos(cx, cy, R, 9); disc(ax, p9[0], p9[1], 1.8, 'sujet')
p4 = pos(cx, cy, R, 4); disc(ax, p4[0], p4[1], 1.8, 'resultat')
line(ax, [(cx, cy), pos(cx, cy, R - 3, 4)], 'resultat', lw=1.6)
p = pos(cx, cy, R + 4.2, 4); text(ax, p[0] + 0.5, p[1], '4', 'resultat', 'm', weight='bold')
arcline(ax, cx, cy, R - 6, 9, 16, 'varie')
text(ax, 66, 50, '9 + 7 = 16', 'varie', 'l')
text(ax, 66, 40, 'l\u2019aiguille montre 4', 'resultat', 'm')
text(ax, 66, 27, '16 \u2212 4 = 12', 'encre', 'l')
text(ax, 66, 20, 'un tour complet', 'fixe', 'm')
save(fig, '43-001')
