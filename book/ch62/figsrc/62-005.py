import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, s = 30, 32, 18
R = 2 ** (1 / 3)
P = [(cx + R * s, cy), (cx - R / 2 * s, cy + R * math.sqrt(3) / 2 * s), (cx - R / 2 * s, cy - R * math.sqrt(3) / 2 * s)]
arrow(ax, (cx - 22, cy), (cx + 36, cy), 'fixe', lw=0.7)
arrow(ax, (cx, cy - 29), (cx, cy + 30), 'fixe', lw=0.7)
poly(ax, P, 'sujet', fill=True)
for i, (a, b) in enumerate([(0, 1), (1, 2), (2, 0)]):
    mx, my = (P[a][0] + P[b][0]) / 2, (P[a][1] + P[b][1]) / 2
    dx, dy = P[b][0] - P[a][0], P[b][1] - P[a][1]
    n = math.hypot(dx, dy); ux, uy = -dy / n, dx / n
    line(ax, [(mx - ux * 1.6, my - uy * 1.6), (mx + ux * 1.6, my + uy * 1.6)], 'varie', lw=1.4)
for (x, y), nm, dx, dy in zip(P, ['$r_1$', '$r_2$', '$r_3$'], [3, -3, -3], [3, 3, -3]):
    disc(ax, x, y, 1.5, 'sujet')
    text(ax, x + dx, y + dy, nm, 'sujet', 'm')
text(ax, 70, 52, 'trois côtés\négaux', 'varie', 'm')
text(ax, 70, 22, 'trois racines\n= trois points', 'sujet', 'm')
text(ax, 86, 60, 'plan complexe', 'fixe', 's', ha='right')
save(fig, '62-005')
