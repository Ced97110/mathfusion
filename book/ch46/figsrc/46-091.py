import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(64)
box(ax, 14, 50, 60, 10, 'autre', label='S₃ : 6 permutations, pas cyclique', size='s')
subs = [('fixe',), ('fixe', 'varie'), ('fixe', 'varie'), ('fixe', 'varie'), ('fixe', 'autre', 'autre')]
xs = [8, 25, 42, 59, 77]
for x, s in zip(xs, subs):
    w = 14 if len(s) < 3 else 18
    cx = x if len(s) < 3 else x + 1
    box(ax, cx - w / 2 + 0, 18, w, 18, 'sujet', fill=False, lw=1.0)
    n = len(s)
    for i, r in enumerate(s):
        disc(ax, cx - (n - 1) * 3.2 + i * 6.4, 27, 2.6, r)
    line(ax, [(44, 50), (cx, 36.5)], 'sujet', lw=0.6)
text(ax, 44, 11, '5 sous-groupes propres : tous cycliques', 'sujet', 's')
text(ax, 2, 3, 'gris : ne rien changer', 'fixe', 's', ha='left')
text(ax, 34, 3, 'orange : échange', 'varie', 's', ha='left')
text(ax, 60, 3, 'violet : rotation', 'autre', 's', ha='left')
save(fig, '46-091')
