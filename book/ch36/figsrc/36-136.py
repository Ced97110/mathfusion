import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(74)
s = 1.8; P = (8, 22)
Q = (P[0] + 30*s*math.sin(math.radians(40)), P[1] + 30*s*math.cos(math.radians(40)))
R = (Q[0] + 20*s*math.sin(math.radians(110)), Q[1] + 20*s*math.cos(math.radians(110)))
line(ax, [P, (P[0], P[1] + 44)], 'fixe', dash=True)
line(ax, [P, Q], 'sujet', lw=1.5); line(ax, [Q, R], 'autre', lw=1.5)
arrow(ax, R, (P[0] + 1.2, P[1] + 0.5), 'resultat', lw=1.4)
arc(ax, P, 11, 50, 90, 'sujet', lw=1.1); arc(ax, P, 26, 23, 50, 'varie', lw=1.1)
for p, t, dx, dy in [(P, 'P', -3, -3), (Q, 'Q', 0, 3.5), (R, 'R', 3, 0)]:
    ax.plot(*p, 'o', color=COL['encre'], ms=2.5, zorder=4); text(ax, p[0] + dx, p[1] + dy, t, 'encre', 'm')
text(ax, *pol(P, 15, 72), r'$40°$', 'sujet', 's'); text(ax, *pol(P, 33, 36.5), r'$27{,}03°$', 'varie', 's')
text(ax, P[0] + 1.5, P[1] + 48, 'N', 'encre', 's')
text(ax, 8, 12, r'port $\to$ navire : $N\,67{,}03°\,E$', 'encre', 'm', ha='left')
text(ax, 8, 5, r'retour : $S\,67{,}03°\,O$', 'resultat', 'm', ha='left')
save(fig, '36-136')
