import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
line(ax, [(44, 6), (44, 58)], 'fixe', dash=True, lw=0.6)
# case 1: two circles overlapping, lens = {0}
r, d, cy = 11.0, 11.0, 34.0
cx1 = 9 + r
a = math.acos(d / (2 * r))
pts = [(cx1 + r * math.cos(t), cy + r * math.sin(t)) for t in [(-a + 2 * a * i / 20) for i in range(21)]]
pts += [(cx1 + d + r * math.cos(t), cy + r * math.sin(t)) for t in [(math.pi - a + 2 * a * i / 20) for i in range(21)]]
poly(ax, pts, 'resultat')
ax.add_patch(Circle((cx1, cy), r, ec=COL['sujet'], fc='none', lw=1.0, zorder=3))
ax.add_patch(Circle((cx1 + d, cy), r, ec=COL['autre'], fc='none', lw=1.0, zorder=3))
text(ax, cx1 - 4.5, cy + r + 3, 'H', 'sujet', 'm', weight='bold'); text(ax, cx1 + d + 4.5, cy + r + 3, 'K', 'autre', 'm', weight='bold')
text(ax, cx1 - 5, cy, '2, 4', 'sujet', 's'); text(ax, cx1 + d + 5, cy, '3', 'autre', 's')
text(ax, cx1 + d / 2, cy, '0', 'resultat', 'm', weight='bold')
text(ax, 22, 12, 'seulement 0 : vrai', 'resultat', 's')
# case 2: H inside K
kx, kr, hr = 66.0, 14.0, 6.5
ax.add_patch(Circle((kx, cy), kr, ec=COL['autre'], fc=FILL['autre'], lw=1.0, zorder=2))
ax.add_patch(Circle((kx - 5, cy + 1), hr, ec=COL['limite'], fc=FILL['limite'], lw=1.0, zorder=3))
text(ax, kx - 5, cy + 1, '0, 3', 'limite', 's')
text(ax, kx + 4, cy - 7.5, '1, 2, 4, 5', 'autre', 's')
text(ax, kx - 12, cy + kr + 2, 'H', 'limite', 'm', weight='bold'); text(ax, kx + 10, cy + kr + 2, 'K', 'autre', 'm', weight='bold')
text(ax, 66, 12, '0 et 3 : faux', 'limite', 's')
save(fig, '45-207')
