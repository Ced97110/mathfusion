import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
cx, cy, R = 44, 40, 22
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=1))
line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', lw=0.6)
line(ax, [(cx - R - 6, cy), (cx + R + 6, cy)], 'sujet', lw=1.8)
text(ax, 12, cy + 4, r'$\mathbb{Q}(r)$ : réels', 'sujet', 's')
text(ax, 44, 76, r'$x^3-2$', 'sujet', 'm')
for k, (l, role) in enumerate([(r'$r$', 'sujet'), (r'$jr$', 'limite'), (r'$j^2r$', 'limite')]):
    a = math.radians(120 * k)
    x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    disc(ax, x, y, 2.2, role)
    if k == 0:
        text(ax, x + 5, y + 4, l, role, 's')
    else:
        text(ax, x - 7, y + (2 if k == 1 else -2), l, role, 's')
text(ax, 44, 6, 'jr et j²r : non réels, absents', 'limite', 's')
save(fig, '63-116')
