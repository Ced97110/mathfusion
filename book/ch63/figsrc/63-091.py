import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(76)
cx, cy, R = 42, 38, 24
pts = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (0, 120, 240)]
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=1))
for p, q in ((pts[0], pts[1]), (pts[1], pts[2]), (pts[2], pts[0])):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy); e = 2.6 / n
    line(ax, [(p[0] + dx * e, p[1] + dy * e), (q[0] - dx * e, q[1] - dy * e)], 'fixe', lw=0.7, dash=True)
disc(ax, pts[0][0], pts[0][1], 2.2, 'sujet')
disc(ax, pts[1][0], pts[1][1], 2.2, 'autre')
disc(ax, pts[2][0], pts[2][1], 2.2, 'autre')
text(ax, pts[0][0] + 4, pts[0][1], r'$r$', 'sujet', 'm', ha='left')
text(ax, pts[1][0] - 3, pts[1][1] + 4, r'$jr$', 'autre', 'm')
text(ax, pts[2][0] - 3, pts[2][1] - 4, r'$j^2r$', 'autre', 'm')
text(ax, cx, cy + 3, r'$p=x^3-2$', 'fixe', 's')
text(ax, cx, cy - 3, r'$d=3$', 'fixe', 's')
text(ax, 44, 4, r'3 racines distinctes : conjugués de $r$', 'resultat', 's')
save(fig, '63-091')
