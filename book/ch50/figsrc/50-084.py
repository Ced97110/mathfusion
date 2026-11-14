import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cx, cy, R = 24, 38, 19
c30 = math.cos(math.radians(30))
P = {'A': (cx, cy + R), 'B': (cx - R * c30, cy - R / 2), 'C': (cx + R * c30, cy - R / 2)}
poly(ax, list(P.values()), 'fixe')
lab = {'A': (cx, cy + R + 3.4), 'B': (cx - R * c30 - 2.5, cy - R / 2 - 3), 'C': (cx + R * c30 + 2.5, cy - R / 2 - 3)}
for k in 'ABC':
    text(ax, *lab[k], k, 'fixe', 's', weight='bold')
    v = P[k]; d = ((cx - v[0]) / R, (cy - v[1]) / R)
    end = (v[0] + d[0] * 1.5 * R, v[1] + d[1] * 1.5 * R)
    line(ax, [(v[0] - d[0] * 1.5, v[1] - d[1] * 1.5), (end[0] + d[0] * 2, end[1] + d[1] * 2)], 'varie', lw=1.0, dash=True)
    text(ax, end[0] + d[0] * 5.2, end[1] + d[1] * 5.2, r'$s_%s$' % k, 'varie', 's', weight='bold')
a0 = math.radians(150); sw = math.radians(300)
pts = [(cx + 4.2 * math.cos(a0 + sw * t / 30), cy + 4.2 * math.sin(a0 + sw * t / 30)) for t in range(31)]
# rotation: counter-clockwise arc around the centre, no axis
pts = [(cx + 4.2 * math.cos(a0 + sw * t / 30), cy + 4.2 * math.sin(a0 + sw * t / 30)) for t in range(31)]
line(ax, pts[:-1], 'sujet', lw=1.4); arrow(ax, pts[-2], pts[-1], 'sujet', lw=1.4)
# right: groups
box(ax, 52, 40, 34, 18, 'sujet')
text(ax, 69, 52, r'$\{e,\ r,\ r^2\}$', 'sujet', 'm')
text(ax, 69, 45, 'rotations : 1 sous-groupe', 'sujet', 's')
for i, k in enumerate('ABC'):
    box(ax, 52, 24 - 0 - i * 0 + 0, 0.01, 0.01, 'fixe', fill=False, lw=0) if False else None
for i, k in enumerate('ABC'):
    y = 33 - 0 + 0
xs3 = [52, 63.4, 74.8]
for k, x in zip('ABC', xs3):
    box(ax, x, 22, 11.2, 9, 'varie', label=r'$\{e,\,s_%s\}$' % k, size='s')
text(ax, 69, 35.5, 'réflexions : 3 sous-groupes', 'varie', 's')
arrow(ax, (33, 49), (51, 49), 'sujet'); arrow(ax, (44, 26.5), (51, 26.5), 'varie')
text(ax, cx, 15, '3 axes pareils', 'varie', 's')
save(fig, '50-084')
