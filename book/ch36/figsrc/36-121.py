import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(72)
s = 1.75
A = (14, 12); t = math.radians(88)
C = (A[0] + 23*s*math.cos(t), A[1] + 23*s*math.sin(t))
F = (C[0], A[1])
arrow(ax, A, (80, 12), 'fixe')
line(ax, [A, C], 'sujet', lw=1.4)
line(ax, [C, F], 'resultat', lw=1.0, dash=True)
disc(ax, C[0], C[1], 2*s, 'varie')
line(ax, [C, (C[0] + 2*s, C[1])], 'varie', lw=0.9)
arc(ax, A, 9, 0, 88, 'varie')
text(ax, 25, 20, r'$88°$', 'varie', 's')
text(ax, 7, 32, '23', 'sujet', 's')
text(ax, 22, 32, r'$h\approx22{,}99$', 'resultat', 's', ha='left')
text(ax, C[0] + 2*s + 3, C[1] + 4, '2', 'varie', 's', ha='left')
text(ax, C[0] + 2*s + 3, C[1] - 4, 'cercle de rayon 2', 'varie', 's', ha='left')
text(ax, 30, 22, r'$22{,}99\div2\approx11{,}49$', 'encre', 'm', ha='left')
text(ax, 30, 15.5, r'$11{,}49>1$ : impossible', 'limite', 'm', ha='left')
save(fig, '36-121')
