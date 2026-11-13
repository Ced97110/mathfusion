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
s = 5.2
A = (8, 8); C = (A[0] + 10*s*math.cos(math.radians(30)), A[1] + 5*s)
F = (C[0], A[1])
arrow(ax, A, (82, 8), 'fixe')
disc(ax, C[0], C[1], 5*s, 'varie')
poly(ax, [A, C, F], 'sujet')
line(ax, [A, C], 'sujet', lw=1.3)
rightangle(ax, F, 90, 180, 2.6, 'resultat')
arc(ax, A, 11, 0, 30, 'varie')
text(ax, 24, 11.5, r'$30°$', 'varie', 's')
text(ax, 14, 24, '10', 'sujet', 's')
text(ax, F[0] + 3, C[1] / 2 + 4, '5', 'varie', 's', ha='left')
text(ax, (A[0] + F[0]) / 2, 3.5, r'$8{,}66$', 'sujet', 's')
text(ax, F[0] + 3, 14, 'angle droit', 'resultat', 's', ha='left')
text(ax, C[0] + 2, C[1] + 12, 'cercle : 1 seul point', 'varie', 's', ha='left')
text(ax, 8, 66, 'discriminant = 0', 'resultat', 'm', ha='left')
save(fig, '36-122')
