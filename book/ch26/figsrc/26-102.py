import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(92)
s = 3.1
def kite(oy, role='sujet', fill=True):
    A = (5, oy); D = pt(A, 5 * s, 40); B = (D[0], 2 * oy - D[1]); O = (D[0], oy); C = (O[0] + 6.218 * s, oy)
    poly(ax, [A, B, C, D], role, fill=fill)
    return A, B, C, D, O
A, B, C, D, O = kite(76, fill=False)
text(ax, A[0] - 3, A[1] + 2.5, 'A', 'sujet'); text(ax, D[0], D[1] + 3, 'D', 'sujet'); text(ax, B[0], B[1] - 3, 'B', 'sujet'); text(ax, C[0] + 3, 76 + 2.5, 'C', 'sujet')
text(ax, 46, 80, '1. Dessiner', 'encre', ha='left', weight='bold'); text(ax, 46, 73, 'le cerf-volant', 'encre', ha='left', size='s')
A, B, C, D, O = kite(46, fill=False)
line(ax, [A, C], 'varie', lw=1.6, dash=True); line(ax, [B, D], 'fixe', dash=True)
square(O, 90, 180, 2.0); arc(A, 8, -40, 40, 'varie')
text(ax, 46, 50, '2. Chercher une symétrie', 'varie', ha='left', weight='bold'); text(ax, 46, 43, 'axe AC : angles de 40°', 'varie', ha='left', size='s')
A, B, C, D, O = kite(16, fill=False)
poly(ax, [A, O, D], 'sujet'); poly(ax, [C, O, D], 'autre')
square(O, 90, 180, 2.0); arc(A, 6, 0, 40, 'varie')
text(ax, *pt(A, 10, 20), '40°', 'varie', 's', ha='left')
text(ax, A[0] + 4.5, A[1] + 8.5, '5', 'sujet', 's')
text(ax, 46, 22, '3. Triangles rectangles', 'encre', ha='left', weight='bold'); text(ax, 46, 15, 'AOD : angle 40°, côté 5', 'sujet', ha='left', size='s')
text(ax, 46, 9, 'COD : côté 7, DO commun', 'autre', ha='left', size='s')
text(ax, 46, 3, 'angle + côté : on s’arrête', 'resultat', ha='left', weight='bold', size='s')
save(fig, '26-102')
