import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(70)
th = 40; E = (10, 16); T = (62, 16 + 52 * math.tan(math.radians(th)))
line(ax, [(62, 8), T], 'fixe', lw=1.4); line(ax, [(4, 8), (84, 8)], 'fixe')
line(ax, [E, (84, 16)], 'fixe', dash=True)
line(ax, [E, T], 'sujet', lw=1.6)
disc(ax, *E, 1.2, 'sujet'); disc(ax, *T, 1.2, 'sujet')
arc(E, 20, 0, th, 'varie'); text(ax, 33.5, 20.5, '40°', 'varie')
text(ax, 10, 22, 'œil', 'sujet'); text(ax, T[0] + 1, T[1] + 4, 'sommet', 'sujet')
text(ax, 72, 19.5, 'horizontale', 'fixe', 's'); text(ax, 26, 42, 'ligne de visée', 'sujet', 's', rot=th)
text(ax, 52, 4, 'sol', 'fixe', 's'); text(ax, 64, 36, 'arbre', 'fixe', 's', ha='left')
text(ax, 22, 63, 'angle d’élévation', 'varie', 'm') if False else None
save(fig, '26-106')
