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
s = 1.8; P = (8, 10)
Q = (P[0] + 30*s*math.sin(math.radians(40)), P[1] + 30*s*math.cos(math.radians(40)))
R = (Q[0] + 20*s*math.sin(math.radians(110)), Q[1] + 20*s*math.cos(math.radians(110)))
line(ax, [P, (P[0], P[1] + 40)], 'fixe', dash=True); line(ax, [(Q[0], Q[1] + 6), (Q[0], Q[1] - 27)], 'fixe', dash=True)
line(ax, [P, Q], 'sujet', lw=1.5); line(ax, [Q, R], 'autre', lw=1.5)
arc(ax, P, 11, 50, 90, 'sujet'); arc(ax, Q, 8, -130, -90, 'sujet'); arc(ax, Q, 8, -90, -20, 'autre')
arc(ax, Q, 21, -130, -20, 'resultat', lw=1.2)
for p, t, dx, dy in [(P, 'P', -3, -3), (Q, 'Q', 0, 9), (R, 'R', 3, 0)]:
    ax.plot(*p, 'o', color=COL['encre'], ms=2.5, zorder=4); text(ax, p[0] + dx, p[1] + dy, t, 'encre', 'm')
text(ax, 11.5, 27, r'$40°$', 'sujet', 's')
text(ax, *pol(Q, 13, -113), r'$40°$', 'sujet', 's'); text(ax, *pol(Q, 13, -50), r'$70°$', 'autre', 's')
text(ax, *pol(Q, 25.5, -75), r'$110°$', 'resultat', 's')
text(ax, P[0] + 1.5, P[1] + 45, 'N', 'encre', 's'); text(ax, Q[0] - 3, Q[1] - 28, 'S', 'encre', 's')
save(fig, '36-131')
