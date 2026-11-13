import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(62)
s = 0.647; A = (6, 14); B = pt(A, 100 * s, 30); C = (B[0], A[1])
line(ax, [(3, 14), (84, 14)], 'fixe'); text(ax, 80, 18, 'canal', 'fixe', 's')
line(ax, [B, C], 'resultat', lw=2.4)
line(ax, [A, C], 'resultat', lw=2.4)
line(ax, [A, B], 'sujet', lw=1.6)
disc(ax, *A, 1.0, 'sujet'); disc(ax, *B, 1.0, 'sujet')
square(C, 180, 90)
arc(A, 13, 0, 30); text(ax, 24, 17.5, '30°', 'varie', 's')
text(ax, 25, 36, '100 m', 'sujet')
brace(ax, A[0], C[0], 12.5, 'resultat', label=r'avance $50\sqrt{3} \approx 86{,}6$ m', down=True, size='m')
text(ax, C[0] + 3, 36, 'éloignement', 'resultat', ha='left', size='s'); text(ax, C[0] + 3, 31, '50 m', 'resultat', ha='left')
text(ax, 44, 57, 'chemin = 2 déplacements', 'encre', 's')
save(fig, '26-100')
