import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(64)
cx, cy, R = 24, 32, 18
disc(ax, cx, cy, R, 'fixe', fill=False)
P = (cx + R * math.cos(math.radians(30)), cy + R * math.sin(math.radians(30)))
line(ax, [(cx, cy), (cx + R, cy)], 'fixe')
line(ax, [(cx, cy), P], 'sujet', lw=1.2)
a = arc(cx, cy, 12, 0, 340)
line(ax, a, 'varie', lw=1.2)
arrow(ax, a[-2], arc(cx, cy, 12, 0, 360)[-1], 'varie')
disc(ax, P[0], P[1], 1.7, 'resultat')
text(ax, 46, 47, r'$t=1$ et $t=13$', 'resultat', 'm', ha='left')
text(ax, 46, 41, 'même point, 3 m', 'resultat', 'm', ha='left')
text(ax, 46, 24, '12 h = un tour', 'varie', 'm', ha='left')
text(ax, 46, 18, r'$12\times 30°=360°$', 'varie', 'm', ha='left')
save(fig, '32-005')
