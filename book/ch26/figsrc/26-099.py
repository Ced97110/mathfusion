import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(58)
s = 2.4; Lm = 10 * s; y = 20
for x0, th, ang, pr in [(4, 0, '0°', '10 m'), (34, 60, '60°', '5 m'), (64, 90, '90°', '0 m')]:
    A = (x0, y); B = pt(A, Lm, th); Fp = (B[0], y)
    line(ax, [(x0 - 1, y), (x0 + 22, y)], 'fixe')
    if th: line(ax, [B, Fp], 'fixe', dash=True)
    if th < 90: line(ax, [A, Fp], 'resultat', lw=3.2)
    else: disc(ax, *A, 1.6, 'resultat')
    if th: line(ax, [A, B], 'sujet', lw=1.2)
    else: line(ax, [A, B], 'sujet', lw=0.7)
    disc(ax, *A, 0.8, 'sujet'); disc(ax, *B, 0.8, 'sujet')
    text(ax, x0 + 12, 49, ang, 'varie', 'l')
    text(ax, x0 + 12, 12, pr, 'resultat', 'm')
    text(ax, x0 + 12, 5, {0: r'$\cos 0° = 1$', 60: r'$\cos 60° = 0{,}5$', 90: r'$\cos 90° = 0$'}[th], 'encre', 's')
text(ax, 44, 55, 'segment AB de 10 m', 'sujet', 's')
save(fig, '26-099')
