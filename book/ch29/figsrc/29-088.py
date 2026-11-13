import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

cx, cy, R = 44, 26, 22
a0, a1 = 90 - 57.3, 90 + 57.3
P = (cx + R * math.cos(math.radians(a1)), cy + R * math.sin(math.radians(a1)))
Q = (cx + R * math.cos(math.radians(a0)), cy + R * math.sin(math.radians(a0)))
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
poly(ax, arcp(cx, cy, R, a0, a1), 'varie')
line(ax, [P, Q], 'resultat', lw=1.8)
line(ax, arcp(cx, cy, R, a0, a1), 'varie', lw=1.8)
line(ax, [(cx, cy), P], 'sujet')
line(ax, [(cx, cy), Q], 'sujet')
line(ax, [(cx, cy), (cx, P[1])], 'fixe', dash=True)
disc(ax, P[0], P[1], 1.0, 'encre'); disc(ax, Q[0], Q[1], 1.0, 'encre')
text(ax, P[0] - 4, P[1] + 1, r'$P$', 'encre', 'm')
text(ax, Q[0] + 4, Q[1] + 1, r'$Q$', 'encre', 'm')
text(ax, cx, cy - 4, r'$O$', 'encre', 'm')
text(ax, 55, 20.5, 'r = 3', 'sujet', 's')
text(ax, cx, 53, 'arc', 'varie', 's')
text(ax, 42.5, 34.2, 'corde', 'resultat', 's', ha='right')
text(ax, cx, 43.2, 'segment circulaire', 'varie', 's', weight='bold')
text(ax, 40, 30, '1', 'fixe', 's')
text(ax, 48, 30, '1', 'fixe', 's')
text(ax, cx, 15, 'angle POQ = 2', 'encre', 's')
save(fig, '29-088')
