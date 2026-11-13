import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(70)
A = (10, 12); C = (66, 12); B = (66, 12 + 56*math.tan(math.radians(40)))
line(ax, [(4, 12), (84, 12)], 'fixe')
poly(ax, [A, C, B], 'sujet')
rmark(ax, C, -1, 1)
arc(ax, A, 10, 0, 40)
text(ax, 26, 15.5, r'40°', 'varie', 's')
text(ax, A[0]-1, A[1]-4.5, 'A : vous', 'sujet', 's', ha='left')
text(ax, C[0], C[1]-4.5, 'C : pied', 'sujet', 's')
text(ax, B[0], B[1]+4, 'B : sommet', 'sujet', 's')
text(ax, 38, 8.5, r'$b$ = 20 m (adjacent)', 'fixe', 's', va='top')
text(ax, C[0]+2, (C[1]+B[1])/2, r'$a$ = ?', 'varie', 'm', ha='left')
text(ax, C[0]+2, (C[1]+B[1])/2-5, 'opposé', 'varie', 's', ha='left')
save(fig, '25-097')
