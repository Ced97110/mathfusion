import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
# left: x^2 - 2 on a number line
f = numberline(ax, 5, 39, 28, -2, 2, step=1, labels=False, arrow_right=False)
for v, l in [(-math.sqrt(2), r'$-\sqrt{2}$'), (math.sqrt(2), r'$\sqrt{2}$')]:
    disc(ax, f(v), 28, 2, 'resultat')
    text(ax, f(v), 35, l, 'resultat', 's')
text(ax, 22, 56, r'$x^2-2$', 'sujet', 'm')
text(ax, 22, 49, '2 racines distinctes', 'resultat', 's')
# right: x^3 - 2 in the plane
cx, cy, R = 66, 28, 12
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=1))
line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', lw=0.6)
line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', lw=0.6)
for k, l in enumerate([r'$r$', r'$jr$', r'$j^2r$']):
    a = math.radians(120 * k)
    x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    disc(ax, x, y, 2, 'resultat')
    text(ax, cx + (R + 5.5) * math.cos(a), cy + (R + 4.5) * math.sin(a), l, 'resultat', 's')
text(ax, 66, 56, r'$x^3-2$', 'sujet', 'm')
text(ax, 66, 49, '3 racines distinctes', 'resultat', 's')
save(fig, '63-099')
