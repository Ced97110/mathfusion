import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(90)
s = 0.5; W = (8, 14); E = (W[0] + 127*s, 14)
B = (W[0] + 164.0*s*math.cos(math.radians(54)), 14 + 164.0*s*math.sin(math.radians(54)))
line(ax, [W, E], 'fixe', lw=1.5)
line(ax, [W, (W[0], 14 + 38)], 'fixe', dash=True); line(ax, [E, (E[0], 14 + 38)], 'fixe', dash=True)
line(ax, [W, B], 'sujet', lw=1.4); line(ax, [E, B], 'autre', lw=1.4)
arc(ax, W, 15, 54, 90, 'varie'); arc(ax, W, 9, 0, 54, 'sujet')
arc(ax, E, 15, 90, 103, 'varie'); arc(ax, E, 9, 103, 180, 'autre')
arc(ax, B, 11, 234, 283, 'resultat', lw=1.2)
for p, t, dx, dy in [(W, 'O', -3.5, 0), (E, 'E', 3.5, 0), (B, 'ballon', 0, 4)]:
    ax.plot(*p, 'o', color=COL['encre'], ms=2.5, zorder=4); text(ax, p[0] + dx, p[1] + dy, t, 'encre', 's')
text(ax, *pol(W, 20, 72), r'$36°$', 'varie', 's'); text(ax, 29, 22, r'$54° = 90° - 36°$', 'sujet', 's')
text(ax, E[0] + 1, 14 + 22, r'$13°$', 'varie', 's', ha='left'); text(ax, E[0] - 17, 22, r'$77° = 90° - 13°$', 'autre', 's')
text(ax, B[0], B[1] - 18, r'$49°$', 'resultat', 's')
text(ax, (W[0] + E[0]) / 2, 8, '127 km', 'fixe', 's')
text(ax, 21, 52, r'$164{,}0$ km', 'sujet', 's'); text(ax, 52, 38, r'$136{,}1$ km', 'autre', 's')
save(fig, '36-137')
