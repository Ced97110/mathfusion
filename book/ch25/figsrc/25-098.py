import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(78)
# small triangle
A = (6, 52); C = (30, 52); B = (30, 52 + 24*math.tan(math.radians(40)))
poly(ax, [A, C, B], 'sujet'); rmark(ax, C, -1, 1)
arc(ax, A, 6, 0, 40)
text(ax, 17, 54.5, '40°', 'varie', 's', ha='left')
text(ax, 18, 48, '20 m', 'fixe', 's')
text(ax, 34, 62, r'$a$', 'varie', 'm', ha='left')
# steps
box(ax, 40, 56, 44, 12, 'sujet', label=r'tan 40° = $a$ / 20')
box(ax, 40, 31, 44, 12, 'varie', label=r'$a$ = 20 × tan 40°')
box(ax, 8, 4, 76, 12, 'resultat', label=r'$a$ ≈ 20 × 0,8391 ≈ 16,78 m')
arrow(ax, (62, 56), (62, 43), 'varie'); text(ax, 65, 49.5, '× 20', 'varie', 's', ha='left')
arrow(ax, (62, 31), (62, 16), 'varie'); text(ax, 65, 23.5, 'calcul', 'varie', 's', ha='left')
text(ax, 17, 72, 'définition', 'sujet', 's')
save(fig, '25-098')
