import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(64)
cx, cy, r = 42, 30, 22
ax.add_patch(Circle((cx, cy), r, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=1.5))
line(ax, [(cx - r - 4, cy), (cx + r + 4, cy)], 'fixe'); line(ax, [(cx, cy - r - 4), (cx, cy + r + 4)], 'fixe')
pts = [(0, 'sujet', '(1, 0)', '0°'), (90, 'varie', '(0, 1)', '90°'), (180, 'varie', r'$(-1,\,0)$', '180°')]
for a, role, lab, ang in pts:
    px, py = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
    line(ax, [(cx, cy), (px, py)], role, lw=1.0)
    disc(ax, px, py, 1.5, role)
text(ax, cx + r + 3, cy + 3, '(1, 0)', 'sujet', 's', ha='left')
text(ax, cx, cy + r + 5, '(0, 1)', 'varie', 's')
text(ax, cx - r - 3, cy + 3, r'$(-1,\,0)$', 'varie', 's', ha='right')
text(ax, cx + 12, cy - 3, '0°', 'sujet', 's')
text(ax, cx + 5, cy + 12, '90°', 'varie', 's')
text(ax, cx - 12, cy - 3, '180°', 'varie', 's')
text(ax, cx, 3, r'une rotation $R(\theta)$ = un point du cercle', 'encre', 's')
save(fig, '73-068')
