import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

fig, ax = canvas(52)
g = 12.0
A = (8.0, g)
L = 70.0
S = (A[0] + L * math.cos(math.radians(18)), g + L * math.sin(math.radians(18)))
line(ax, [(4, g), (84, g)], 'fixe')
line(ax, [A, S], 'sujet', lw=1.3)
ax.add_patch(Arc(A, 2 * 20, 2 * 20, theta1=0, theta2=18, color=COL['varie'], lw=1.2, zorder=3))
disc(ax, A[0], A[1], 1.2, 'sujet')
text(ax, A[0], g - 3.5, 'A', 'sujet', 'm')
text(ax, S[0] + 1, S[1] + 3, 'S', 'sujet', 's')
text(ax, 40, g + 3.5, 'α = 18°', 'varie', 'm', weight='bold')
text(ax, 54, g - 3.5, 'sol', 'fixe', 's')
text(ax, 34, 33, 'visée AS', 'sujet', 's')
text(ax, 44, 46, 'α : élévation en A', 'varie', 'm', weight='bold')
save(fig, '38-036')
