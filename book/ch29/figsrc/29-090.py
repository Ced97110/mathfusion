import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

cx, cy, R = 44, 28, 22
P = (cx + R * math.cos(math.radians(140)), cy + R * math.sin(math.radians(140)))
Q = (cx + R * math.cos(math.radians(40)), cy + R * math.sin(math.radians(40)))
S = (cx + R * math.cos(math.radians(-40)), cy + R * math.sin(math.radians(-40)))
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
line(ax, arcp(cx, cy, R, 40, 140), 'autre', lw=2.0)
line(ax, [P, Q], 'sujet', lw=2.0)
line(ax, [(cx, cy), S], 'fixe', lw=1.4)
for p, c in ((P, 'sujet'), (Q, 'sujet'), ((cx, cy), 'fixe'), (S, 'fixe')):
    disc(ax, p[0], p[1], 0.9, c)
text(ax, P[0] - 4, P[1], r'$P$', 'encre', 'm')
text(ax, Q[0] + 4, Q[1], r'$Q$', 'encre', 'm')
text(ax, cx - 4, cy + 1, r'$O$', 'encre', 'm')
text(ax, cx, P[1] - 4.5, 'corde', 'sujet', 'm', weight='bold')
text(ax, cx, 54.5, 'arc (courbe)', 'autre', 's')
text(ax, 38, 17, 'rayon', 'fixe', 's')
save(fig, '29-090')
