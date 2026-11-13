import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(44)
A = (6, 12); B = (80, 12); C = (80, 18.2)
poly(ax, [A, B, C], 'sujet')
text(ax, 43, 8, '12', 'encre', 'm')
text(ax, 83, 15, '1', 'encre', 'm', ha='left')
arcp(ax, A, 22, 0, 4.76)
arrow(ax, (30, 21), (28.6, 13.2), 'resultat')
text(ax, 30, 24, r'$\theta$ : angle aigu', 'resultat', 's')
box(ax, 8, 31, 70, 10, 'resultat', label=r'$\theta=\arctan\frac{1}{12}\approx4{,}76°$', size='m')
save(fig, '33-093')
