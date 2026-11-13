import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(66)
s = 60/168
A = (8, 12); C = (8+168*s, 12); B = (C[0], 12+132.44*s)
poly(ax, [A, C, B], 'sujet'); rmark(ax, C, -1, 1)
arc(ax, A, 12, 0, 38.25)
text(ax, 23, 15.5, '38,25°', 'varie', 's', ha='left')
text(ax, (A[0]+C[0])/2, 7, '168 m', 'fixe', 's')
text(ax, C[0]+2, (C[1]+B[1])/2, r'$h$', 'sujet', 'l', ha='left')
text(ax, C[0]+2, (C[1]+B[1])/2-6, '≈ 132,44 m', 'resultat', 's', ha='left', va='top') if False else None
text(ax, 44, 62, r'$h$ = 168 × tan 38,25°', 'sujet', 'm')
text(ax, 44, 55.5, '≈ 168 × 0,78834 ≈ 132,44 m', 'resultat', 's')
save(fig, '25-101')
