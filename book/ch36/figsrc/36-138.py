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
s = 0.5; A = (8, 30)
B = (A[0] + 90*s, A[1]); T = pol(A, 120*s, 50); F = (T[0], A[1])
poly(ax, [A, B, T], 'sujet')
line(ax, [A, B, T, A], 'sujet', lw=1.4)
line(ax, [T, F], 'varie', lw=1.2, dash=True)
rightangle(ax, F, 180, 90, 2.4, 'varie')
arc(ax, A, 10, 0, 50, 'varie', lw=1.1)
text(ax, *pol(A, 16, 22), r'$50°$', 'varie', 's')
text(ax, (A[0] + B[0]) / 2, A[1] - 4, r'$c=90$', 'sujet', 's')
text(ax, 13, 56, r'$b=120$', 'sujet', 's')
text(ax, F[0] - 2, 52, r'$h\approx91{,}92$', 'varie', 's', ha='right')
text(ax, 8, 18, 'aire = ½ × 90 × 91,92', 'encre', 'm', ha='left')
text(ax, 8, 11, '= ½ × 120 × 90 × sin 50°', 'encre', 'm', ha='left')
text(ax, 8, 4, r'$\approx4\,136{,}6$', 'resultat', 'm', ha='left')
save(fig, '36-138')
