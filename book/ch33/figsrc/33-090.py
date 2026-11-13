import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(52)
A = (6, 8); B = (42, 8); C = (42, 26)
poly(ax, [A, B, C], 'fixe')
poly(ax, [B, (B[0]-2.2, B[1]), (B[0]-2.2, B[1]+2.2), (B[0], B[1]+2.2)], 'fixe', fill=False, lw=0.6)
text(ax, 24, 4.3, '2', 'encre', 'm')
text(ax, 45, 17, '1', 'encre', 'm', ha='left')
arcp(ax, A, 14, 0, 26.565)
text(ax, 25, 11.5, r'$\theta$', 'resultat', 'm')
text(ax, 14, 46, r'$\mathrm{arccot}\,2=\arctan\frac{1}{2}$', 'encre', 'm', ha='left')
box(ax, 54, 26, 31, 9, 'autre', label=r'$\mathrm{cotan}\,\theta=2/1$', size='s')
box(ax, 54, 8, 31, 9, 'sujet', label=r'$\tan\theta=1/2$', size='s')
text(ax, 69.5, 21.5, 'même angle', 'encre', 's')
text(ax, 69.5, 39, 'environ 26,57°', 'resultat', 's')
save(fig, '33-090')
