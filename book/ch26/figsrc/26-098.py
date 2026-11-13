import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(66)
th = 60; L = 50; A = (8, 8); B = pt(A, L, th); C = (B[0], A[1])
line(ax, [(4, 8), (46, 8)], 'fixe'); text(ax, 44, 3.5, r'$l$', 'fixe')
line(ax, [A, C], 'fixe', lw=1.4)
line(ax, [A, B], 'sujet', lw=1.6)
line(ax, [C, B], 'resultat', lw=2.6)
for p, r in [(A, 'sujet'), (B, 'sujet'), (C, 'fixe')]: disc(ax, *p, 1.0, r)
text(ax, A[0] - 2.5, A[1] + 3, 'A', 'sujet'); text(ax, B[0], B[1] + 3.5, 'B', 'sujet'); text(ax, C[0] + 3, 4, 'C', 'fixe')
square(C, 180, 90)
arc(A, 11, 0, th); text(ax, 24, 13, r'$\theta$', 'varie')
text(ax, 14, 36, 'AB', 'sujet'); text(ax, C[0] + 5, 30, 'BC', 'resultat')
text(ax, 50, 56, 'BC est opposé à', 'resultat', ha='left', size='s'); text(ax, 50, 51, r'$\theta$ ; AB est la plus', 'resultat', ha='left', size='s'); text(ax, 50, 46, 'longue (hypoténuse)', 'resultat', ha='left', size='s')
text(ax, 50, 35, r'$\sin\theta = BC \, / \, AB$', 'encre', ha='left')
text(ax, 50, 28, r'$BC = AB \times \sin\theta$', 'resultat', ha='left')
text(ax, 50, 19, r'$10 \times 0{,}866 = 8{,}66$ m', 'resultat', ha='left', size='s')
save(fig, '26-098')
