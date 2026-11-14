import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, r = 44, 42, 26
disc(ax, cx, cy, r, 'sujet')
a = math.atan2(0.8, 0.6)
from matplotlib.patches import Ellipse
ax.add_patch(Ellipse((cx, cy), 2 * r, 0.4 * r, angle=math.degrees(a) - 90, fill=False, ec=COL['varie'], lw=1.0, ls='--', zorder=3))
ex, ey = r * math.cos(a), r * math.sin(a)
line(ax, [(cx - ex, cy - ey), (cx + ex, cy + ey)], 'resultat', lw=1.6)
disc(ax, cx + ex, cy + ey, 2.0, 'resultat'); disc(ax, cx - ex, cy - ey, 2.0, 'resultat')
disc(ax, cx, cy, 0.9, 'encre')
text(ax, cx + ex + 1, cy + ey + 5, r'$(1,-1,1)$', 'resultat', 's', ha='left')
text(ax, cx - ex - 1, cy - ey - 5, r'$(-1,1,-1)$', 'resultat', 's', ha='right')
text(ax, cx + 3, cy - 4, 'centre', 'encre', 's', ha='left')
text(ax, 44, 74, 'la sphère a tourné', 'sujet', 'm')
text(ax, 44, 5, 'deux points opposés en place', 'resultat', 's')
text(ax, 84, 18, 'tour autour de l’axe', 'varie', 's', ha='right')
save(fig, '72-147')
