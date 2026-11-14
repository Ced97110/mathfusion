import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Circle
fig, ax = canvas(56)
text(ax, 44, 50, 'n tient la place des heures', 'fixe', 'm')
for i, (n, lab, sub) in enumerate([(2, 'ℤ/2', '2 heures'), (3, 'ℤ/3', '3 heures'), (4, 'ℤ/4', '4 heures'), (None, 'ℤ/n', '$n$ heures')]):
    cx = 12 + i * 21.5; cy = 31
    if n:
        disc(ax, cx, cy, 9, 'fixe', fill=False)
        for k in range(n):
            a = math.radians(90 - 360 * k / n); disc(ax, cx + 9 * math.cos(a), cy + 9 * math.sin(a), 1.6, 'sujet')
        role = 'sujet'
    else:
        ax.add_patch(Circle((cx, cy), 9, ec=COL['varie'], fc='none', ls='--', lw=0.8, zorder=2))
        text(ax, cx, cy, '$n$', 'varie', 'xl'); role = 'varie'
    text(ax, cx, 16, lab, role, 'm', weight='bold'); text(ax, cx, 10, sub, role, 's')
save(fig, '51-048')
