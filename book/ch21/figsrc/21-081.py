import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
fig, ax = canvas(66)
cy, r = 40, 15
for cx in (22, 66):
    ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))
ax.add_patch(Wedge((22, cy), r, -90, 90, fc=FILL['sujet'], ec=COL['sujet'], lw=0.9, zorder=3))
ax.add_patch(Wedge((66, cy), r, 90, 210, fc=FILL['autre'], ec=COL['autre'], lw=0.9, zorder=3))
line(ax, [(22, cy - r), (22, cy + r)], 'sujet')
for a in (90, 210, 330):
    line(ax, [(66, cy), (66 + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))], 'autre')
text(ax, 29, cy, r'$\frac{1}{2}$', 'sujet', 'm')
text(ax, 66 + 8 * math.cos(math.radians(150)), cy + 8 * math.sin(math.radians(150)), r'$\frac{1}{3}$', 'autre', 'm')
text(ax, 22, 18, 'pizza coupée en 2', 'sujet', 's')
text(ax, 66, 18, 'pizza coupée en 3', 'autre', 's')
text(ax, 44, 8, 'deux parts, tailles différentes', 'encre', 's')
save(fig, '21-081')
