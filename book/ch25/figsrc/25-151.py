import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax, c, r, a0, a1, role, lw=1.0):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
fig, ax = canvas(80)
x0, k = 29, 8.0
def grp(y, title, rows):
    text(ax, 2, y+8, title, 'encre', 'm', ha='left', weight='bold')
    for i, (lab, v, role) in enumerate(rows):
        yy = y - 6*i
        text(ax, x0-2, yy, lab, role, 's', ha='right')
        box(ax, x0, yy-2, max(v*k, 1.4), 4, role, r=0.3)
        text(ax, x0+max(v*k, 1.4)+1.5, yy, f'{v:.4f}'.replace('.', ','), role, 's', ha='left')
grp(64, 'Angle doublé : 10° → 20°', [('tan 10°', 0.1763, 'sujet'), ('2 × tan 10°', 0.3526, 'fixe'), ('tan 20°', 0.3640, 'resultat')])
grp(30, '40° → 80°', [('tan 40°', 0.8391, 'sujet'), ('2 × tan 40°', 1.6782, 'fixe'), ('tan 80°', 5.6713, 'resultat')])
save(fig, '25-151')
