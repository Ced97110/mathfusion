import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(60)
g = 12; foot = (72, g); top = (72, 50); P1 = (8, g); P2 = (30, g)
box(ax, 38, g - 5, 28, 5, 'fixe', r=0.3, label='rivière', size='s')
line(ax, [(4, g), (80, g)], 'fixe', lw=1.0)
line(ax, [foot, top], 'sujet', lw=2.2); disc(ax, top[0], top[1], 1.4, 'sujet')
text(ax, 72, 55, 'hauteur ?', 'sujet', 's')
line(ax, [foot, (P2[0] + 0, g)], 'limite', dash=True)
text(ax, 56, 21, 'distance inconnue', 'limite', 's')
for P, k in ((P1, '1'), (P2, '2')):
    line(ax, [P, top], 'varie', lw=1.0); disc(ax, P[0], P[1], 1.4, 'varie')
    ang = math.degrees(math.atan2(top[1] - P[1], top[0] - P[0]))
    ax.add_patch(Arc(P, 14, 14, theta1=0, theta2=ang, color=COL['varie'], lw=1.0, zorder=4))
text(ax, 21, 15.5, 'angle 1', 'varie', 's'); text(ax, 39.5, 15.5, 'angle 2', 'varie', 's', ha='left')
save(fig, '25-144')
