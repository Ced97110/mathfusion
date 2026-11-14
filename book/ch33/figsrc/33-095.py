import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(54)
F = (42, 12); T = (42 - 30.8, 12); Hh = (42, 12 + 33.6)
line(ax, [(4, 12), (52, 12)], 'fixe')
line(ax, [Hh, T], 'varie', lw=1.2)
line(ax, [F, Hh], 'sujet', lw=2.0)
line(ax, [T, F], 'autre', lw=2.0)
arcp(ax, T, 9, 0, 47.49)
text(ax, T[0]+12.5, 16.2, r'$\theta$', 'resultat', 'm')
text(ax, 44, 28, '168 cm', 'sujet', 's', ha='left')
text(ax, 27, 8, 'ombre : 154 cm', 'autre', 's')
text(ax, 22, 44, 'rayon du soleil', 'varie', 's')
box(ax, 57, 31, 29, 10, 'fixe', label=r'$\tan\theta=168/154$', size='s')
box(ax, 57, 15, 29, 10, 'resultat', label=r'$\theta\approx47{,}49°$', size='s')
save(fig, '33-095')
