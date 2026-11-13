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
def panel(x, y, kind):
    role = 'resultat' if kind == 0 else 'limite'
    if kind == 0:
        for bx in (x + 1, x + 21): box(ax, bx, y, 18, 20, 'resultat')
        pions(ax, spots(x + 1, y, 18, 20, 3, cols=2), 'sujet'); pions(ax, spots(x + 21, y, 18, 20, 3, cols=2), 'sujet')
    elif kind == 1:
        for bx in (x + 1, x + 14): box(ax, bx, y, 12, 20, 'sujet')
        pions(ax, spots(x + 1, y, 12, 20, 3, cols=2), 'sujet'); pions(ax, spots(x + 14, y, 12, 20, 3, cols=2), 'sujet')
        box(ax, x + 27, y, 12, 20, 'limite', dash=True)
    elif kind == 2:
        box(ax, x + 1, y, 16, 20, 'sujet'); box(ax, x + 23, y, 16, 20, 'sujet')
        pions(ax, spots(x + 1, y, 16, 20, 3, cols=2), 'sujet'); pions(ax, spots(x + 23, y, 16, 20, 2, cols=2), 'sujet')
        pions(ax, [(x + 20, y + 10)], 'limite', r=1.9)
    else:
        box(ax, x + 1, y, 24, 20, 'sujet', fill=False); box(ax, x + 15, y, 24, 20, 'autre', fill=False)
        pions(ax, [(x + 6, y + 6), (x + 6, y + 14), (x + 33, y + 6), (x + 33, y + 14), (x + 12, y + 10)][:5], 'sujet')
        pions(ax, [(x + 20, y + 10)], 'limite', r=1.9)
panel(3, 42, 0); panel(45, 42, 1); panel(3, 12, 2); panel(45, 12, 3)
text(ax, 23, 37.5, 'partition', 'resultat', 'm', weight='bold')
text(ax, 65, 37.5, 'bo\u00eete vide', 'limite', 'm')
text(ax, 23, 7.5, 'pion sans bo\u00eete', 'limite', 'm')
text(ax, 65, 7.5, 'pion dans deux bo\u00eetes', 'limite', 's')
save(fig, '43-012')
