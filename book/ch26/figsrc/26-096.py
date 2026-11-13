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
th = 60; L = 50; A = (8, 12); B = pt(A, L, th); Fp = (B[0], A[1])
line(ax, [(4, 12), (46, 12)], 'fixe'); text(ax, 44, 7.5, r'$l$', 'fixe')
line(ax, [A, Fp], 'resultat', lw=2.6)
line(ax, [B, Fp], 'fixe', dash=True)
line(ax, [A, B], 'sujet', lw=1.6)
disc(ax, *A, 1.0, 'sujet'); disc(ax, *B, 1.0, 'sujet'); disc(ax, *Fp, 1.0, 'resultat')
text(ax, A[0] - 2.5, A[1] + 3.5, 'A', 'sujet'); text(ax, B[0], B[1] + 3.5, 'B', 'sujet'); text(ax, Fp[0] + 3, 8, 'F', 'resultat')
square(Fp, 180, 90)
arc(A, 11, 0, th); text(ax, 24, 17, r'$\theta$', 'varie')
text(ax, 16, 40, 'AB', 'sujet'); text(ax, 21, 8, 'EF', 'resultat')
text(ax, 50, 54, '1. mesurer AB', 'sujet', ha='left'); text(ax, 50, 53 - 6, '10 m', 'sujet', ha='left')
text(ax, 50, 40, r'2. cherche $\cos 60°$', 'varie', ha='left'); text(ax, 50, 34, '0,5', 'varie', ha='left')
text(ax, 50, 24, r'3. multiplie', 'resultat', ha='left'); text(ax, 50, 18, r'$10 \times 0{,}5 = 5$ m', 'resultat', ha='left')
save(fig, '26-096')
