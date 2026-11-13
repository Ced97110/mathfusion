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

fig, ax = canvas(66)
box(ax, 4, 46, 80, 12, 'sujet', label='r\u00e8gle : m\u00eame chiffre des unit\u00e9s', size='m')
arrow(ax, (44, 45.5), (44, 36), 'fixe', both=True, lw=1.0)
x0, pitch = 3, 8.4
for c in range(10):
    role = 'resultat' if c == 3 else 'fixe'
    bx = x0 + c * pitch
    box(ax, bx, 12, 6.6, 22, role)
    for ri, y in enumerate((17.5, 28.5)):
        v = c + 10 * ri
        disc(ax, bx + 3.3, y, 2.4, 'resultat' if c == 3 else 'fixe', label=str(v) if c in (0, 3) else None, size='s')
text(ax, 44, 5, '10 paquets de 2 entiers', 'resultat', 'm')
save(fig, '43-015')
