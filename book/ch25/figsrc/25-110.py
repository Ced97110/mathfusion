import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(74)
k = 7
B = (10, 12); A = (B[0]+5*k, 12); C = (B[0], 12+7*k)
poly(ax, [A, B, C], 'sujet'); rmark(ax, B, 1, 1)
arc(ax, A, 9, 180-54.46, 180)
text(ax, A[0]-14, A[1]+4.5, 'A', 'sujet', 'm') if False else None
text(ax, A[0]+2, A[1]-1, 'A', 'sujet', 'm', ha='left')
text(ax, B[0]-2, B[1]-4.5, 'B', 'sujet', 'm')
text(ax, C[0], C[1]+4, 'C', 'sujet', 'm')
text(ax, 27, 7.5, 'AB = 5 cm : adjacent', 'fixe', 's')
text(ax, 13, 36, 'BC = 7 cm', 'varie', 's', ha='left')
text(ax, 13, 31.5, 'opposé à A', 'varie', 's', ha='left')
text(ax, 60, 52, r'tan A = 7 / 5 = 1,4', 'sujet', 's') if False else None
text(ax, 62, 50, 'tan A = 7 / 5', 'sujet', 's')
text(ax, 62, 43, '= 1,4', 'sujet', 's')
text(ax, 62, 33, 'A ≈ 54,46°', 'resultat', 'm')
save(fig, '25-110')
