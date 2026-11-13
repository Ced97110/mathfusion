import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(80)
s = 12; O = (12, 18); U = (O[0] + 3*s, O[1]); V = pol(O, 4*s, 60)
arrow(ax, O, (82, O[1]), 'fixe', lw=0.8); arrow(ax, O, (O[0], 70), 'fixe', lw=0.8)
line(ax, [O, U], 'sujet', lw=1.5); line(ax, [O, V], 'autre', lw=1.5); line(ax, [U, V], 'resultat', lw=1.5, dash=True)
arc(ax, O, 9, 0, 60, 'varie', lw=1.1)
for p, role in [(O, 'encre'), (U, 'sujet'), (V, 'autre')]:
    ax.plot(*p, 'o', color=COL[role], ms=3, zorder=4)
text(ax, O[0] - 3, O[1] - 3, 'O', 'encre', 's')
text(ax, (O[0] + U[0]) / 2, O[1] - 4, '3', 'sujet', 's'); text(ax, 17, 40, '4', 'autre', 's')
text(ax, *pol(O, 14, 28), r'$60°$', 'varie', 's')
text(ax, 62, 42, r'$d\approx3{,}61$', 'resultat', 'm', ha='left')
text(ax, 66, 74, 'plan des nombres', 'fixe', 's')
text(ax, 44, 5, r'$d^2=9+16-12=13$', 'encre', 'm')
save(fig, '36-141')
