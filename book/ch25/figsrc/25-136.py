import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(54)
O = (36, 3); u = 6
P = lambda x, y, z=0: iso(x, y, z, O, u)
poly(ax, [P(0, 0), P(8, 0), P(8, 6), P(0, 6)], 'fixe')
text(ax, 15, 17, 'sol (un plan)', 'fixe', 's')
base = P(1, 3); top = P(1, 3, 4); foot = P(6, 3)
poly(ax, [base, top, foot], 'sujet')
line(ax, [base, top], 'sujet', lw=1.6); line(ax, [top, foot], 'sujet', lw=1.6)
line(ax, [base, foot], 'varie', lw=1.8)
text(ax, base[0] - 6, (base[1] + top[1]) / 2, 'mât', 'sujet', 's')
text(ax, (top[0] + foot[0]) / 2 + 3, (top[1] + foot[1]) / 2 + 5, 'câble', 'sujet', 's')
text(ax, (base[0] + foot[0]) / 2 + 3, (base[1] + foot[1]) / 2 - 3.5, '10 m', 'varie', 's')
a1 = math.degrees(math.atan2(top[1] - foot[1], top[0] - foot[0])); a2 = math.degrees(math.atan2(base[1] - foot[1], base[0] - foot[0])) + 360
ax.add_patch(Arc(foot, 14, 14, theta1=a1, theta2=a2, color=COL['limite'], lw=1.2, zorder=4))
text(ax, foot[0] + 3, foot[1] - 4, 'angle câble-sol', 'limite', 's', ha='left')
line(ax, [P(1.7, 3), P(1.7, 3, 0.7), P(1, 3, 0.7)], 'fixe', lw=0.8)
text(ax, base[0] - 1, base[1] - 5, 'angle droit', 'fixe', 's', ha='left')
save(fig, '25-136')
