import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# left: the plane, multiplication by i
cx, cy, R = 20, 40, 12
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.5, zorder=1, ls='--'))
arrow(ax, (cx - R - 3, cy), (cx + R + 4, cy), 'fixe', lw=0.5)
arrow(ax, (cx, cy - R - 3), (cx, cy + R + 4), 'fixe', lw=0.5)
disc(ax, cx + R, cy, 1.3, 'sujet'); disc(ax, cx, cy + R, 1.3, 'resultat')
t = [math.radians(90 * k / 20) for k in range(21)]
pts = [(cx + 7 * math.cos(v), cy + 7 * math.sin(v)) for v in t]
line(ax, pts, 'varie', lw=1.0); arrow(ax, pts[-3], pts[-1], 'varie', lw=1.0)
text(ax, cx, 70, 'plan', 'sujet', 's')
text(ax, cx, 63, r'$\times\, i$ : quart de tour', 'varie', 's')
text(ax, cx, 18, '1 axe : le point', 'fixe', 's')
# right: space, isometric axes
o = (62, 32); L = 20
for name, v in (('x', (1, 0, 0)), ('y', (0, 1, 0)), ('z', (0, 0, 1))):
    arrow(ax, iso(0, 0, 0, o), iso(v[0] * L, v[1] * L, v[2] * L, o), 'fixe', lw=0.6)
t = [2 * math.pi * k / 40 for k in range(41)]
line(ax, [iso(11 * math.cos(v), 11 * math.sin(v), 0, o) for v in t], 'varie', lw=1.0)
line(ax, [iso(0, 11 * math.cos(v), 11 * math.sin(v), o) for v in t], 'autre', lw=1.0)
text(ax, 62, 66, 'espace', 'sujet', 's')
text(ax, 62, 60, '3 nombres : est, nord, hauteur', 'sujet', 's')
text(ax, 62, 10, 'tours autour de toute droite', 'varie', 's')
text(ax, 62, 3.5, 'quelle règle abandonner ?', 'autre', 's')
save(fig, '39-145')
