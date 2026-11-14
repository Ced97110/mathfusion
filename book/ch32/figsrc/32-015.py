import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(66)
cx, cy, R = 48, 28, 20
k = R * 0.5
disc(ax, cx, cy, R, 'fixe', fill=False)
line(ax, [(cx - R - 4, cy), (cx + R + 4, cy)], 'fixe')
line(ax, [(cx - R - 6, cy + k), (cx + R + 6, cy + k)], 'sujet', lw=1.3)
P = (cx + R * math.cos(math.radians(30)), cy + k)
Q = (cx - R * math.cos(math.radians(30)), cy + k)
line(ax, [(cx, cy), P], 'fixe')
line(ax, [(cx, cy), Q], 'fixe')
line(ax, arc(cx, cy, 9, 0, 30), 'varie', lw=1.2)
line(ax, arc(cx, cy, 24, 0, 150), 'autre', lw=1.2)
disc(ax, P[0], P[1], 1.6, 'resultat')
disc(ax, Q[0], Q[1], 1.6, 'resultat')
text(ax, P[0] + 3.5, P[1] + 3.5, r'$P$', 'resultat', 'm')
text(ax, Q[0] - 3.5, Q[1] + 3.5, r"$P'$", 'resultat', 'm')
text(ax, cx + R + 16, cy + k, r'$y=k$', 'sujet', 'm')
text(ax, cx + 14, cy + 3.5, r'$\theta$', 'varie', 'm')
text(ax, cx, cy + 24 + 5, r'$180°-\theta$', 'autre', 'm')
save(fig, '32-015')
