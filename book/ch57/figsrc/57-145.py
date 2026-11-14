import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 10.0; ox, oy = 22.0, 26.0
P = lambda x, y: (ox + x * u, oy + y * u)
XMIN, XMAX, YMIN, YMAX = -2, 5, -2, 3
def seg(c, role, lw):
    # classe c : x - 2y = c, i.e. y = (x - c)/2, restreinte au cadre
    pts = []
    for x in (XMIN, XMAX):
        y = (x - c) / 2
        if YMIN <= y <= YMAX: pts.append((x, y))
    for y in (YMIN, YMAX):
        x = 2 * y + c
        if XMIN <= x <= XMAX: pts.append((x, y))
    pts = sorted(set(pts))
    if len(pts) >= 2: line(ax, [P(*pts[0]), P(*pts[-1])], role, lw=lw)
special = {0: ('sujet', 1.6), -1: ('autre', 1.3), 1: ('varie', 1.3)}
for c in range(-8, 9):
    if c in special: continue
    seg(c, 'fixe', 0.45)
for c, (r, lw) in special.items(): seg(c, r, lw)
for i in range(XMIN, XMAX + 1):
    for j in range(YMIN, YMAX + 1):
        c = i - 2 * j
        if c in special: disc(ax, *P(i, j), 1.0, special[c][0])
        else: disc(ax, *P(i, j), 0.5, 'fixe')
text(ax, 75, P(5, 3)[1] + 1, r'$(1\,;\,1)+N$', 'autre', 's', ha='left')
text(ax, 75, P(5, 2.5)[1] - 3, r'$N$', 'sujet', 's', ha='left')
text(ax, 75, P(5, 2)[1] - 7, r'$(1\,;\,0)+N$', 'varie', 's', ha='left')
text(ax, 44, 62, 'chaque point sur une seule droite', 'encre', 's')
save(fig, '57-145')
