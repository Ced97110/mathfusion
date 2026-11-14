import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(58)
cx, cy, r = 44, 30, 10
for a in (0, 90, 180, 270):
    line(ax, [(cx, cy), (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))], 'fixe', lw=0.5)
ax.add_patch(Arc((cx, cy), 2 * r, 2 * r, theta1=0, theta2=270, color=COL['varie'], lw=2.0, zorder=4))
box(ax, 6, 24, 16, 12, 'sujet', label='3', size='l')
box(ax, 66, 24, 16, 12, 'autre', label=r'$r_3$', size='l')
arrow(ax, (23, 30), (32, 30), 'varie'); arrow(ax, (56, 30), (65, 30), 'varie')
for x, t in ((14, r'1  choisir $k$'), (44, '2  compter'), (74, '3  nommer')):
    text(ax, x, 50, t, 'encre', 's')
text(ax, 14, 15, r'$k=3$', 'sujet', 's'); text(ax, 44, 13, '3 quarts de tour', 'varie', 's'); text(ax, 74, 15, r'nom $r_3$', 'autre', 's')
text(ax, 44, 5, r'$\eta(3)=r_3$', 'resultat', 'l')
save(fig, '45-018')
