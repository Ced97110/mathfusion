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
box(ax, 3, 26, 50, 32, 'sujet', fill=False)
box(ax, 33, 26, 52, 32, 'autre', fill=False)
text(ax, 5, 54.5, 'bo\u00eete 1', 'sujet', 's', ha='left')
text(ax, 83, 54.5, 'bo\u00eete 2', 'autre', 's', ha='right')
X, Y, Z = (43, 46), (14, 34), (74, 34)
def seg(P, Q, role, dash=False):
    d = math.hypot(Q[0]-P[0], Q[1]-P[1]); u = ((Q[0]-P[0])/d, (Q[1]-P[1])/d)
    line(ax, [(P[0]+u[0]*2.6, P[1]+u[1]*2.6), (Q[0]-u[0]*2.6, Q[1]-u[1]*2.6)], role, lw=1.1, dash=dash)
seg(X, Y, 'resultat'); seg(X, Z, 'resultat'); seg(Y, Z, 'limite', True)
disc(ax, *X, 2.4, 'sujet', label='$x$', size='s'); disc(ax, *Y, 2.4, 'sujet', label='$y$', size='s'); disc(ax, *Z, 2.4, 'autre', label='$z$', size='s')
text(ax, 25, 43.5, 'oui', 'resultat', 's'); text(ax, 62, 43.5, 'oui', 'resultat', 's'); text(ax, 44, 30, 'non', 'limite', 's')
text(ax, 44, 17, '$x$ est avec $y$ et avec $z$', 'resultat', 'm')
text(ax, 44, 9, '$y$ n\u2019est pas avec $z$', 'limite', 'm')
save(fig, '43-011')
