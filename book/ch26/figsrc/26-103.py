import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(74)
s = 6; y0 = 38
A = (6, y0); D = pt(A, 5 * s, 40); Bp = (D[0], 2 * y0 - D[1]); O = (D[0], y0); C = (O[0] + math.sqrt(49 - 3.2139**2) * s, y0)
poly(ax, [A, Bp, C, D], 'sujet')
line(ax, [(2, y0), (84, y0)], 'resultat', lw=1.4, dash=True)
line(ax, [Bp, D], 'fixe', dash=True)
square(O, 90, 180, 2.0)
for q in (D, Bp):
    mx = (O[0] + q[0]) / 2; my = (O[1] + q[1]) / 2
    line(ax, [(mx - 1.2, my), (mx + 1.2, my)], 'varie', lw=1.2)
for p, q in [(A, D), (A, Bp)]:
    mx = (p[0] + q[0]) / 2; my = (p[1] + q[1]) / 2
    line(ax, [(mx - 1.4, my - 1.4), (mx + 1.4, my + 1.4)], 'varie', lw=1.2) if False else None
text(ax, A[0] - 3, y0 + 3, 'A', 'sujet'); text(ax, D[0], D[1] + 3, 'D', 'sujet'); text(ax, Bp[0], Bp[1] - 3, 'B', 'sujet'); text(ax, C[0] + 3, y0 + 3, 'C', 'sujet')
text(ax, O[0] + 3, y0 - 3.5, 'O', 'fixe')
text(ax, 14, y0 + 15, 'AB = AD', 'sujet', 's'); text(ax, 60, y0 + 16, 'CB = CD', 'sujet', 's')
text(ax, 44, 8, 'AC : axe de symétrie', 'resultat'); text(ax, 44, 2.5 + 64, 'AC et BD font un angle droit', 'encre', 's')
save(fig, '26-103')
