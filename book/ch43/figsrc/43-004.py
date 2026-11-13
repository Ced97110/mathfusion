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

fig, ax = canvas(64)
x0, pitch, r = 7.5, 6.6, 2.35
ys = [54, 46, 38]
for c in range(12):
    role = 'sujet' if c == 1 else 'fixe'
    for ri, y in enumerate(ys):
        v = c + 12 * ri
        disc(ax, x0 + c * pitch, y, r, role, label=str(v) if c < 2 else None, size='s')
    bx = x0 + c * pitch
    arrow(ax, (bx, 34.8), (bx, 26.5), role, lw=0.8)
    box(ax, bx - 2.9, 16, 5.8, 10, role, label=str(c) if c < 2 else None, size='s')
text(ax, 85, 46, '\u2026', 'fixe', 'l')
text(ax, 44, 60.5, 'tous les entiers', 'fixe', 'm')
brace(ax, x0 - 2.9, x0 + 11 * pitch + 2.9, 15, 'resultat', label='12 groupes = 12 positions')
text(ax, 44, 3, '109 est dans le groupe de 1', 'sujet', 'm')
save(fig, '43-004')
