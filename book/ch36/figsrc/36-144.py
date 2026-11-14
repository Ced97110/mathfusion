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
s = 10; O = (12, 14); u = (O[0] + 3*s, O[1]); v = (O[0], O[1] + 4*s)
poly(ax, [O, u, v], 'fixe')
line(ax, [O, u], 'sujet', lw=1.6); line(ax, [O, v], 'autre', lw=1.6); line(ax, [u, v], 'resultat', lw=1.6, dash=True)
rightangle(ax, O, 0, 90, 3, 'varie')
text(ax, (O[0] + u[0]) / 2, O[1] - 4, 'u', 'sujet', 'm'); text(ax, O[0] - 4, 36, 'v', 'autre', 'm')
text(ax, 32, 36, '5', 'resultat', 'm'); text(ax, 21, 21, r'$90°$', 'varie', 's')
text(ax, 50, 52, r'$u\cdot v=3\times4\times0=0$', 'varie', 's', ha='left')
text(ax, 50, 44, r'$9+16=25$', 'encre', 's', ha='left')
text(ax, 50, 36, r'$d=5$ : plus de correction', 'resultat', 's', ha='left')
text(ax, 50, 24, r'$u\perp v$', 'varie', 'm', ha='left')
save(fig, '36-144')
