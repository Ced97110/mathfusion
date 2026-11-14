import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 24, 31, 15
P = [(cx + R * math.cos(math.radians(90 - 30 * k)), cy + R * math.sin(math.radians(90 - 30 * k))) for k in range(12)]
line(ax, [P[k] for k in (0, 3, 6, 9, 0)], 'sujet', lw=1.1)
line(ax, [P[k] for k in (0, 4, 8, 0)], 'autre', lw=1.1)
for k, p in enumerate(P):
    r = 'encre' if k == 0 else ('sujet' if k % 3 == 0 else ('autre' if k % 4 == 0 else 'fixe'))
    disc(ax, p[0], p[1], 1.8, r)
text(ax, 24, 54, r'$\mathbb{Z}/12\mathbb{Z}$', 'encre', 'm', weight='bold')
arrow(ax, (43, 31), (49, 31), 'varie')
for i in range(4):
    for j in range(3):
        r = 'encre' if (i, j) == (0, 0) else ('sujet' if j == 0 else ('autre' if i == 0 else 'fixe'))
        box(ax, 52 + 7 * i, 20 + 7 * j, 6.4, 6.4, r, r=0.3, lw=0.6)
text(ax, 66, 54, r'$\mathbb{Z}/4\times\mathbb{Z}/3$', 'encre', 'm', weight='bold')
text(ax, 66, 14, '2-Sylow : 4', 'sujet', 's')
text(ax, 84, 31, '3-Sylow : 3', 'autre', 's', rot=90)
save(fig, '50-249')
