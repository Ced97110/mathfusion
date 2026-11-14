import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax, c, r, a0, a1, role, lw=1.0):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
fig, ax = canvas(66)
ox, oy = 8, 10
poly(ax, [(ox, oy), (ox+60, oy), (ox+60, oy+45)], 'fixe')
for b, role in ((20, 'resultat'), (40, 'varie'), (60, 'sujet')):
    line(ax, [(ox+b, oy), (ox+b, oy+0.75*b)], role, lw=1.6)
line(ax, [(ox, oy), (ox+60, oy+45)], 'fixe', lw=1.2)
arc(ax, (ox, oy), 12, 0, 36.87, 'encre', 1.2)
text(ax, ox+15, oy+3.2, 'angle', 'encre', 's')
text(ax, ox+27, oy+5.5, 'flèche', 'resultat', 's'); text(ax, ox+47, oy+5.5, 'droite', 'varie', 's')
text(ax, ox+71, oy+22, 'arbre', 'sujet', 's')
text(ax, 44, 62, 'même angle', 'encre', 'm'); text(ax, 44, 56, 'même rapport', 'encre', 'm')
save(fig, '25-150')
