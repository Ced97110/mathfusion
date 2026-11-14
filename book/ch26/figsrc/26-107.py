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
th = math.degrees(math.atan(22 / 34))
E1 = (6, 50); T1 = (40, 28); E2 = (50, 30); T2 = (84, 52)
text(ax, 22, 64, 'dépression', 'sujet', 'l'); text(ax, 66, 64, 'élévation', 'autre', 'l')
line(ax, [E1, (44, 50)], 'fixe', dash=True); line(ax, [E1, T1], 'sujet', lw=1.6)
disc(ax, *E1, 1.2, 'sujet'); disc(ax, *T1, 1.2, 'sujet')
arc(E1, 14, -th, 0, 'sujet'); text(ax, 24, 45.5, r'$\theta$', 'sujet')
text(ax, 8, 55, 'œil', 'sujet'); text(ax, 40, 23, 'bateau', 'sujet', 's')
line(ax, [E2, (86, 30)], 'fixe', dash=True); line(ax, [E2, T2], 'autre', lw=1.6)
disc(ax, *E2, 1.2, 'autre'); disc(ax, *T2, 1.2, 'autre')
arc(E2, 14, 0, th, 'autre'); text(ax, 68, 34.5, r'$\theta$', 'autre')
text(ax, 52, 24.5, 'œil', 'autre'); text(ax, 80, 57.5, 'falaise', 'autre', 's')
text(ax, 22, 12, 'regard vers le bas', 'sujet', 's'); text(ax, 66, 12, 'regard vers le haut', 'autre', 's')
text(ax, 44, 4, 'mesuré depuis l’horizontale', 'fixe', 's')
save(fig, '26-107')
