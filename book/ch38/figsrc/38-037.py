import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

fig, ax = canvas(62)
g = 14.0
B = (6.0, g)
L = 44.0
S = (B[0] + L * math.cos(math.radians(21.25)), g + L * math.sin(math.radians(21.25)))
line(ax, [(2, g), (52, g)], 'fixe')
line(ax, [B, S], 'autre', lw=1.3)
ax.add_patch(Arc(B, 2 * 14, 2 * 14, theta1=0, theta2=21.25, color=COL['autre'], lw=1.2, zorder=3))
disc(ax, B[0], B[1], 1.2, 'autre')
text(ax, B[0], g - 3.5, 'B', 'autre', 'm')
text(ax, S[0] + 1, S[1] + 3, 'S', 'autre', 's')
text(ax, 34, g + 2.2, 'β = 21,25°', 'autre', 's', weight='bold')
text(ax, 26, 46, 'β : élévation en B', 'autre', 'm', weight='bold')
# la même lettre, deux endroits de la formule
box(ax, 58, 36, 28, 9, 'autre', label=r'$\sin\beta$', size='m')
box(ax, 58, 14, 28, 9, 'autre', label=r'$\beta-\alpha$', size='m')
text(ax, 72, 47.5, 'en haut de la fraction', 'fixe', 's')
text(ax, 72, 11, 'en bas de la fraction', 'fixe', 's')
arrow(ax, (57, 40.5), (S[0] + 1.5, S[1] + 0.5), 'autre', curve=0.15)
arrow(ax, (57, 18.5), (S[0] + 2, S[1] - 3), 'autre', curve=-0.15)
save(fig, '38-037')
