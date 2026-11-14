import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(98)
s = 6; y0 = 72
A = (6, y0); D = pt(A, 5 * s, 40); Bp = (D[0], 2 * y0 - D[1]); O = (D[0], y0); C = (O[0] + math.sqrt(49 - 3.2139**2) * s, y0)
poly(ax, [A, Bp, C, D], 'sujet')
line(ax, [A, C], 'fixe', dash=True); line(ax, [Bp, D], 'fixe', dash=True)
line(ax, [O, D], 'varie', lw=2.4)
square(O, 90, 180, 2.0)
arc(A, 9, 0, 40, 'encre'); arc(A, 9, -40, 0, 'encre'); text(ax, 17.5, y0 + 3.6, '40°', 'encre', 's')
arc(C, 8, 180 - 27.33, 180 + 27.33, 'resultat'); text(ax, C[0] - 11, y0 + 3.5, r'$\theta$', 'resultat')
text(ax, A[0] - 3, A[1] + 3, 'A', 'sujet'); text(ax, D[0], D[1] + 3, 'D', 'sujet'); text(ax, Bp[0], Bp[1] - 3, 'B', 'sujet'); text(ax, C[0] + 3, y0 + 3, 'C', 'sujet')
text(ax, O[0] - 3, y0 - 3, 'O', 'fixe'); text(ax, O[0] + 3.5, y0 + 9, r'$x$', 'varie')
text(ax, 14, y0 + 12, '5 cm', 'sujet', 's'); text(ax, 56, y0 + 14, '7 cm', 'sujet', 's')
text(ax, 44, 42, r'1. $x = 5 \times \sin 40°$', 'varie')
text(ax, 44, 34, r'2. $\sin\theta = x \, / \, 7$', 'resultat')
text(ax, 44, 26, r'3. $\theta = \arcsin(x \, / \, 7) \approx 27{,}33°$', 'resultat', 's')
text(ax, 44, 17, r'angle BCD $= 2\theta \approx 54{,}66°$', 'resultat', 'm')
save(fig, '26-101')
