import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
cx, cy, R = 40, 40, 25
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=1))
arrow(ax, (cx - R - 8, cy), (cx + R + 12, cy), 'fixe', lw=0.8)
arrow(ax, (cx, cy - R - 8), (cx, cy + R + 8), 'fixe', lw=0.8)
text(ax, cx + R + 10, cy - 3, 'réels', 'fixe', 's')
text(ax, cx + 9, cy + R + 8, 'imaginaires', 'fixe', 's')
pts = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (0, 120, 240)]
poly(ax, pts, 'sujet')
for (x, y), role in zip(pts, ('resultat', 'sujet', 'sujet')):
    disc(ax, x, y, 1.8, role)
disc(ax, cx, cy, 0.8, 'fixe')
text(ax, cx - 3, cy - 3, '0', 'fixe', 's')
line(ax, [(cx, cy), (pts[0][0], pts[0][1])], 'fixe', dash=True)
text(ax, cx + R * 0.5, cy + 3, '1,26', 'resultat', 's')
text(ax, pts[0][0] - 3.5, pts[0][1] - 5, 'réelle', 'resultat', 's')
text(ax, pts[1][0] - 3, pts[1][1] + 4.5, 'non réelle', 'sujet', 's')
text(ax, pts[2][0] - 3, pts[2][1] - 4.5, 'non réelle', 'sujet', 's')
save(fig, '65-014')
