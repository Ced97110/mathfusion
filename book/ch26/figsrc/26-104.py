import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(82)
s = 4.4; y0 = 56
A = (6, y0); D = pt(A, 5 * s, 40); O = (D[0], y0); C = (O[0] + 6.218 * s, y0)
poly(ax, [A, O, D], 'sujet'); poly(ax, [C, O, D], 'autre')
line(ax, [O, D], 'varie', lw=2.6)
square(O, 180, 90, 1.8) if False else None
text(ax, O[0] + 4, O[1] + 8, 'DO', 'varie')
text(ax, 14, y0 + 18, 'triangle AOD', 'sujet', 's'); text(ax, 62, y0 + 18, 'triangle COD', 'autre', 's')
text(ax, 44, 45, 'DO sert aux deux calculs', 'encre', 's')
box(ax, 3, 28, 38, 10, 'resultat', label='DO = 3,2139… cm', size='s')
box(ax, 50, 28, 35, 10, 'resultat', label='angle 54,66°', size='m')
arrow(ax, (41, 33), (50, 33), 'resultat')
box(ax, 3, 8, 38, 10, 'limite', label='DO arrondi : 3,21', size='s')
box(ax, 50, 8, 35, 10, 'limite', label='angle 54,59°', size='m')
arrow(ax, (41, 13), (50, 13), 'limite')
text(ax, 44, 41, 'entier', 'resultat', 's'); text(ax, 44, 23, 'arrondi : faux', 'limite', 's')
save(fig, '26-104')
