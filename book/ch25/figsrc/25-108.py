import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(96)
k = 6.5
C = (60, 52); A = (C[0]-7*k, 52); B = (C[0], 52+5*k)
poly(ax, [A, C, B], 'sujet'); rmark(ax, C, -1, 1)
arc(ax, A, 9, 0, 35.54)
text(ax, A[0]+11, A[1]+3, 'angle ?', 'varie', 's', ha='left')
text(ax, (A[0]+C[0])/2, 47.5, 'adjacent : 7', 'fixe', 's')
text(ax, C[0]+2, (C[1]+B[1])/2, 'opposé : 5', 'varie', 's', ha='left')
box(ax, 4, 22, 80, 16, 'resultat')
text(ax, 44, 33.5, r'5 ÷ 7 ≈ 0,714  →  arctan', 'resultat', 's')
text(ax, 44, 26.5, 'angle ≈ 35,54°', 'resultat', 'm')
box(ax, 4, 2, 80, 16, 'limite')
text(ax, 44, 13.5, r'7 ÷ 5 = 1,4  →  arctan', 'limite', 's')
text(ax, 44, 6.5, 'faux : ≈ 54,46°, autre angle', 'limite', 's')
save(fig, '25-108')
