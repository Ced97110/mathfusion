import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 24, 31, 19
pos = lambda h: (cx + R * math.cos(math.radians(90 - 30 * h)), cy + R * math.sin(math.radians(90 - 30 * h)))
poly(ax, [pos(h) for h in (0, 3, 6, 9)], 'sujet')
poly(ax, [pos(h) for h in (0, 4, 8)], 'limite', fill=False, lw=1.3)
a, b = pos(0), pos(6); ax.plot([a[0], b[0]], [a[1], b[1]], color=COL['resultat'], lw=1.8, zorder=1.8)
for h in range(12):
    p = pos(h)
    if h in (0, 3, 6, 9): disc(ax, *p, 3, 'sujet', label=str(h), size='s')
    elif h in (4, 8): disc(ax, *p, 3, 'limite', label=str(h), size='s')
    else: disc(ax, *p, 1.3, 'fixe')
text(ax, 50, 52, r"$P'=\{0,3,6,9\}$", 'sujet', 's', ha='left')
text(ax, 50, 40, r"$\{0,6\}$ : dans $P'$", 'resultat', 's', ha='left')
text(ax, 50, 28, r"$\{0,4,8\}$ : hors de $P'$", 'limite', 's', ha='left')
text(ax, 50, 22, 'pas une puissance de 2', 'limite', 's', ha='left')
save(fig, '50-101')
