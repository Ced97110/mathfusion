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
s = 7.0; x0 = 4
cases = [(4, r'$\cos=-0{,}25$ : un triangle', 'resultat', 76), (5, r'$\cos=-1$ : aplati', 'varie', 50), (8, r'$\cos=-4{,}25$ : impossible', 'limite', 24)]
for L, lab, role, y in cases:
    line(ax, [(x0, y + 11), (x0 + L*s, y + 11)], 'fixe', lw=2.0)
    text(ax, x0 + L*s/2, y + 14.5, str(L), 'fixe', 's')
    line(ax, [(x0, y + 5), (x0 + 2*s, y + 5)], 'sujet', lw=2.0)
    line(ax, [(x0 + 2*s, y + 5), (x0 + 5*s, y + 5)], 'autre', lw=2.0)
    text(ax, x0 + s, y + 8, '2', 'sujet', 's'); text(ax, x0 + 3.5*s, y + 8, '3', 'autre', 's')
    text(ax, 44, y - 0.5, lab, role, 'm')
save(fig, '36-126')
