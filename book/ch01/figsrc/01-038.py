import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def link(ax, p, q, r, role, curve=0.0, lw=1.0):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r), role, lw=lw, curve=curve)
def node(ax, x, y, label, ring=False):
    from matplotlib.patches import Circle
    ax.add_patch(Circle((x, y), 2.5, ec=COL['limite' if ring else 'sujet'], fc=FILL['sujet'], lw=1.2 if ring else 0.8, zorder=2))
    text(ax, x, y, label, 'sujet', 's')
fig, ax = canvas(70)
text(ax, 44, 64, 'Horloge : 11 → 12 → 1', 'limite', 'm')
text(ax, 22, 55, 'Retour au départ', 'sujet', 'm', weight='bold')
L = [(22, 47), (33, 36), (22, 25), (11, 36)]
for i, (x, y) in enumerate(L): node(ax, x, y, str(i), ring=(i == 0))
for i in range(3): link(ax, L[i], L[i+1], 2.8, 'sujet', -0.25)
link(ax, L[3], L[0], 2.8, 'limite', -0.25)
text(ax, 22, 10, 'interdit : axiome 1', 'limite', 's', weight='bold')
text(ax, 66, 55, 'Retour sur un autre', 'sujet', 'm', weight='bold')
R = [(50, 44), (60, 44), (70, 44), (82, 34), (70, 24)]
for i, (x, y) in enumerate(R): node(ax, x, y, str(i), ring=(i == 2))
for i in range(4): link(ax, R[i], R[i+1], 2.5, 'sujet')
arrow(ax, (70, 26.5), (70, 41.5), 'limite')
text(ax, 66, 10, 'interdit : axiome 2', 'limite', 's', weight='bold')
save(fig, '01-038')
