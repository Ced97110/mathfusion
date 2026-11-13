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
th = 30; P1 = (22, 18); P2 = (22 + 32 / math.tan(math.radians(th)) , 50)
P2 = (22 + 32 / math.tan(math.radians(th)), 50)
line(ax, [(4, 18), (84, 18)], 'fixe'); line(ax, [(4, 50), (84, 50)], 'fixe')
ext = 10
d = (math.cos(math.radians(th)), math.sin(math.radians(th)))
line(ax, [(P1[0] - ext * d[0], P1[1] - ext * d[1]), (P2[0] + 4 * d[0], P2[1] + 4 * d[1])], 'sujet', lw=1.6)
disc(ax, *P1, 1.0, 'sujet'); disc(ax, *P2, 1.0, 'sujet')
arc(P1, 14, 0, th, 'resultat'); text(ax, P1[0] + 20.5, P1[1] + 2.2, '30°', 'resultat')
arc(P2, 14, 180, 180 + th, 'resultat'); text(ax, P2[0] - 20.5, P2[1] - 2.2, '30°', 'resultat')
text(ax, 12, 23, 'parallèle', 'fixe', 's'); text(ax, 12, 55, 'parallèle', 'fixe', 's')
text(ax, 55, 33, 'sécante', 'sujet', 's', rot=th) if False else None
text(ax, 44, 8, 'angles alternes-internes', 'resultat'); text(ax, 44, 62, 'égaux de part et d’autre', 'resultat', 's')
save(fig, '26-110')
