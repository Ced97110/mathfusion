import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(92)
Q = (44, 80); L = 24
pP = pol(Q, L, -130); pR = pol(Q, L, -20); pS = pol(Q, L + 4, -90)
line(ax, [Q, pS], 'fixe', dash=True)
line(ax, [Q, pP], 'sujet', lw=1.5); line(ax, [Q, pR], 'autre', lw=1.5)
arc(ax, Q, 12, -130, -90, 'sujet', lw=1.2); arc(ax, Q, 12, -90, -20, 'autre', lw=1.2)
ax.plot(*Q, 'o', color=COL['encre'], ms=2.5, zorder=4)
text(ax, Q[0], Q[1] + 4, 'Q', 'encre', 'm'); text(ax, Q[0] + 5, Q[1] - L - 2, 'sud', 'encre', 's')
text(ax, *pol(Q, 17, -115), r'$40°$', 'sujet', 's'); text(ax, *pol(Q, 17, -55), r'$70°$', 'autre', 's')
text(ax, 44, 42, 'de part et d’autre du sud', 'encre', 's')
k = 70/110; x0 = 9; y = 34
line(ax, [(x0, y), (x0 + 40*k, y)], 'sujet', lw=3); line(ax, [(x0 + 40*k, y), (x0 + 110*k, y)], 'autre', lw=3)
ax.plot([x0 + 40*k], [y], '|', color=COL['encre'], ms=8, zorder=4)
text(ax, x0 + 20*k, y + 4, r'$40°$', 'sujet', 's'); text(ax, x0 + 75*k, y + 4, r'$70°$', 'autre', 's')
brace(ax, x0, x0 + 110*k, y - 2, 'resultat', down=True, label=r'$40°+70°=110°$', depth=2.4)
save(fig, '36-132')
