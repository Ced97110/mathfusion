import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax, c, r, a0, a1, role, lw=1.0):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
fig, ax = canvas(70)
x0, k = 4, 50/26.71
text(ax, 2, 66, r'écart : $\tan 2A - 2\tan A$', 'encre', 'm', ha='left')
rows = [('A = 10°', 0.0113, '0,0113'), ('A = 40°', 3.9931, '3,9931'), ('A = 44°', 26.71, '28,64 − 1,93')]
for i, (lab, g, val) in enumerate(rows):
    y = 50 - 15*i
    text(ax, 2, y+6.5, lab, 'sujet', 's', ha='left')
    text(ax, 24, y+6.5, val, 'varie', 's', ha='left')
    box(ax, x0, y-2, max(g*k, 0.6), 4, 'varie', r=0.2)
text(ax, 2, 11.5, 'A = 45°', 'sujet', 's', ha='left')
box(ax, x0, 1.5, 80, 6, 'limite', dash=True, r=0.2)
text(ax, 44, 4.5, '2A = 90° : tan 2A n’existe pas', 'limite', 's')
save(fig, '25-152')
