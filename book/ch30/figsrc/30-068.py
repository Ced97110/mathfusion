import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(58)
C, A, B = (30, 10), (80, 10), (30, 50)
line(ax, [C, A], 'fixe'); line(ax, [A, B], 'fixe'); line(ax, [C, B], 'sujet', lw=2.4)
ax.add_patch(Arc(A, 24, 24, theta1=141.3, theta2=180, color=COL['varie'], lw=1.2))
ax.add_patch(Arc(B, 22, 22, theta1=270, theta2=321.3, color=COL['autre'], lw=1.2))
line(ax, [(34, 10), (34, 14), (30, 14)], 'fixe')
text(ax, 64, 15.6, '$a$', 'varie', 'm'); text(ax, 36.9, 35.6, '$b$', 'autre', 'm')
text(ax, 27, 36, r'opposé à $a$', 'sujet', 's', ha='right')
text(ax, 27, 24, r'adjacent à $b$', 'sujet', 's', ha='right')
text(ax, 60, 34, 'hypoténuse', 'fixe', 's')
text(ax, 45, 6, 'angle droit', 'fixe', 's')
save(fig, '30-068')
