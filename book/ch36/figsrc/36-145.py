import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(100)
f = numberline(ax, 10, 76, 78, 0, 180, step=90, labels=False, arrow_right=False)
line(ax, [(f(0), 86), (f(180), 86)], 'sujet', lw=3)
ax.plot([f(90)], [78], 'o', color=COL['varie'], ms=5, zorder=4)
text(ax, f(0), 72, '0°', 'encre', 's'); text(ax, f(90), 71, '90° : Pythagore', 'varie', 's'); text(ax, f(180), 72, '180°', 'encre', 's')
text(ax, 44, 92, 'loi des cosinus : tous les angles', 'sujet', 's')
A = (10, 14); s = 0.4; B = (A[0] + 90*s, A[1]); C = pol(A, 120*s, 50)
poly(ax, [A, B, C], 'sujet'); line(ax, [A, B, C, A], 'sujet', lw=1.3)
arc(ax, A, 8, 0, 50, 'varie', lw=1.1)
text(ax, *pol(A, 13, 20), r'$50°$', 'varie', 's')
text(ax, (B[0] + C[0]) / 2 + 6, (B[1] + C[1]) / 2 + 2, '92,82', 'resultat', 's')
text(ax, (A[0] + C[0]) / 2 - 4, (A[1] + C[1]) / 2 + 3, '120', 'sujet', 's'); text(ax, (A[0] + B[0]) / 2, A[1] - 4, '90', 'sujet', 's')
text(ax, 56, 44, r'$92{,}82\div\sin50°$', 'resultat', 's', ha='left')
text(ax, 56, 37, r'$\approx121{,}2$', 'resultat', 'm', ha='left')
text(ax, 56, 28, 'même nombre pour', 'encre', 's', ha='left'); text(ax, 56, 22, 'les côtés 120 et 90', 'encre', 's', ha='left')
save(fig, '36-145')
