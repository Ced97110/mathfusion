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
th = math.degrees(math.atan(42 / 56)); O = (14, 52); N = (70, 10); P = (14, 10)
poly(ax, [(4, 10), P, O, (4, 52)], 'fixe')
line(ax, [O, (84, 52)], 'sujet', dash=True); line(ax, [(4, 10), (84, 10)], 'sujet')
line(ax, [O, N], 'resultat', lw=1.6)
disc(ax, *O, 1.0, 'resultat'); disc(ax, *N, 1.0, 'resultat')
arc(O, 16, -th, 0); arc(N, 14, 180 - th, 180)
text(ax, 34.5, 47, r'$\theta$', 'varie'); text(ax, 52, 15.5, r'$\theta$', 'varie')
text(ax, 62, 57, 'dépression', 'varie', 's'); text(ax, 46, 4.5, 'élévation', 'varie', 's')
text(ax, 11, 56, 'O', 'resultat'); text(ax, 74, 5, 'N', 'resultat'); text(ax, 17.5, 6, 'P', 'fixe')
text(ax, 62, 33, 'ligne de visée', 'resultat', 's', rot=-37)
save(fig, '26-105')
