import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(56)
C = (20, 24); r = 17
P = lambda rr, a: (C[0] + rr * math.cos(math.radians(a)), C[1] + rr * math.sin(math.radians(a)))
ax.add_patch(Circle(C, r, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
arrow(ax, (C[0] - r - 2, C[1]), (C[0] + r + 3, C[1]), 'fixe', lw=0.7)
arrow(ax, (C[0], C[1] - r - 2), (C[0], C[1] + r + 3), 'fixe', lw=0.7)
arrow(ax, C, P(r, 60), 'sujet', lw=1.5)
arrow(ax, C, P(r, 30), 'autre', lw=1.5)
ax.add_patch(Arc(C, 18, 18, theta1=30, theta2=60, color=COL['varie'], lw=1.5, zorder=3))
text(ax, 28, 43.5, r'$u$ : 60°', 'sujet', 's')
text(ax, 44, 31, r'$v$ : 30°', 'autre', 's')
text(ax, 36.5, 38.5, r'$\alpha-\beta$', 'varie', 's')
box(ax, 50, 38, 36, 14, 'fixe', label='composantes\n' + r'$0{,}5\times0{,}8660+0{,}8660\times0{,}5$', size='s')
text(ax, 68, 35, '=', 'varie', 'l', weight='bold')
box(ax, 50, 20, 36, 12, 'fixe', label='théorème\n' + r'$1\times1\times\cos 30°$', size='s')
arrow(ax, (68, 19.5), (68, 14), 'fixe')
box(ax, 50, 4, 36, 10, 'resultat', label=r'$\cos(\alpha-\beta)=0{,}8660$', size='s')
save(fig, '41-138')
