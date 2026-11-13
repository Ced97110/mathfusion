import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 31, 56, 'H', 'sujet', 'xl', weight='bold'); text(ax, 44, 56, '∩', 'varie', 'xl', weight='bold'); text(ax, 57, 56, 'K', 'autre', 'xl', weight='bold')
text(ax, 44, 48, 'inter : dans les deux à la fois', 'varie', 's')
r, d, cy = 12.0, 12.0, 26.0
cx1 = 44 - d / 2
a = math.acos(d / (2 * r))
pts = [(cx1 + r * math.cos(t), cy + r * math.sin(t)) for t in [(-a + 2 * a * i / 20) for i in range(21)]]
pts += [(cx1 + d + r * math.cos(t), cy + r * math.sin(t)) for t in [(math.pi - a + 2 * a * i / 20) for i in range(21)]]
poly(ax, pts, 'varie')
ax.add_patch(Circle((cx1, cy), r, ec=COL['sujet'], fc='none', lw=1.0, zorder=3))
ax.add_patch(Circle((cx1 + d, cy), r, ec=COL['autre'], fc='none', lw=1.0, zorder=3))
text(ax, cx1 - 5.5, cy, '2, 4', 'sujet', 's'); text(ax, cx1 + d + 6, cy, '3', 'autre', 's')
text(ax, 44, cy, '0', 'varie', 'm', weight='bold')
text(ax, 44, 6, 'partie commune de H et K', 'varie', 's')
save(fig, '45-208')
