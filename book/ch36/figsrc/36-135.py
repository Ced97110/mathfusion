import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(70)
s = 1.3; Q = (16, 36)
P = (Q[0] + 30*s, Q[1]); R90 = (Q[0], Q[1] + 20*s); R110 = pol(Q, 20*s, 110)
line(ax, [P, R90], 'fixe', lw=1.2, dash=True); line(ax, [Q, R90], 'fixe', lw=1.2, dash=True)
line(ax, [Q, P], 'sujet', lw=1.5); line(ax, [Q, R110], 'autre', lw=1.5); line(ax, [P, R110], 'resultat', lw=1.5)
rightangle(ax, Q, 0, 90, 3, 'fixe'); arc(ax, Q, 9, 0, 110, 'varie', lw=1.1)
for p, t, dx, dy in [(Q, 'Q', -2, -3.5), (P, 'P', 3, 0)]:
    ax.plot(*p, 'o', color=COL['encre'], ms=2.5, zorder=4); text(ax, p[0] + dx, p[1] + dy, t, 'encre', 'm')
text(ax, 38, Q[1] - 4, '30', 'sujet', 's'); text(ax, 5.5, 45.4, '20', 'autre', 's')
text(ax, *pol(Q, 14, 42), r'$110°$', 'varie', 's')
text(ax, 38, 23, r'angle droit : $d\approx36{,}06$', 'fixe', 'm', ha='left')
text(ax, 38, 16, r'$110°$ : $d\approx41{,}36$', 'resultat', 'm', ha='left')
text(ax, 38, 9, r'$-(-410{,}4)=+410{,}4$', 'varie', 'm', ha='left')
save(fig, '36-135')
