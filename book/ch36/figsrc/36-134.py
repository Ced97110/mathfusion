import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(96)
s = 1.5; Q = (52, 82)
P = (Q[0] - 30*s, Q[1]); R = pol(Q, 20*s, -70)
poly(ax, [P, Q, R], 'fixe')
line(ax, [P, Q], 'sujet', lw=1.5); line(ax, [Q, R], 'autre', lw=1.5); line(ax, [P, R], 'resultat', lw=1.5, dash=True)
arc(ax, Q, 7, 180, 290, 'varie', lw=1.1)
for p, t, dx, dy in [(P, 'P', -3, 0), (Q, 'Q', 0, 4), (R, 'R', 3, -2)]:
    ax.plot(*p, 'o', color=COL['encre'], ms=2.5, zorder=4); text(ax, p[0] + dx, p[1] + dy, t, 'encre', 'm')
text(ax, 30, 86, '30', 'sujet', 's'); text(ax, R[0] + 5, (Q[1] + R[1]) / 2 + 4, '20', 'autre', 's')
text(ax, Q[0] - 14, Q[1] - 12, r'$110°$', 'varie', 's')
text(ax, 20, 62, r'$d\approx41{,}36$', 'resultat', 's')
text(ax, 8, 44, r'$30^2+20^2=1\,300$', 'encre', 'm', ha='left')
text(ax, 8, 35, r'$\cos110°\approx-0{,}3420$', 'encre', 'm', ha='left')
text(ax, 8, 26, r'$1\,300+410{,}4=1\,710{,}4$', 'encre', 'm', ha='left')
text(ax, 8, 17, r'$d=\sqrt{1\,710{,}4}\approx41{,}36$', 'resultat', 'm', ha='left')
save(fig, '36-134')
