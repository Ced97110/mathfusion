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

fig, ax = canvas(54)
text(ax, 20, 49, 'paquets', 'fixe', 'm'); text(ax, 68, 49, 'm\u00eame paquet ?', 'fixe', 'm')
box(ax, 3, 14, 22, 30, 'sujet'); box(ax, 28, 14, 14, 30, 'varie')
pa = [(14, 34), (14, 22)]; pb = [(35, 28)]
pions(ax, pa, 'sujet'); pions(ax, pb, 'varie')
text(ax, 18, 34, '$a$', 'sujet', 's'); text(ax, 18, 22, "$a'$", 'sujet', 's'); text(ax, 39.5, 28, '$b$', 'varie', 's')
arrow(ax, (44, 34), (53, 34), 'varie', lw=1.0); text(ax, 48.5, 37, 'répondre', 'varie', 's')
arrow(ax, (53, 24), (44, 24), 'resultat', lw=1.0); text(ax, 48.5, 21, 'regrouper', 'resultat', 's')
rows = [(r"$a$ et $a'$ : oui", 'resultat'), ('$a$ et $b$ : non', 'limite'), ("$a'$ et $b$ : non", 'limite')]
for i, (s, role) in enumerate(rows):
    box(ax, 55, 36 - i * 11, 30, 8.5, role, label=s, size='s')
text(ax, 44, 8, 'on retrouve les m\u00eames paquets', 'resultat', 's')
save(fig, '43-014')
