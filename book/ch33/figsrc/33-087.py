import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(54)
x0, x1 = 10, 70
f = numberline(ax, x0, x1, 30, 0, 15, step=5, arrow_right=False)
arrow(ax, (f(5), 32), (f(15), 32), 'varie', curve=-0.45)
text(ax, f(10), 43, r'$\times 3$', 'varie', 'm')
arrow(ax, (f(15), 22.5), (f(5), 22.5), 'resultat', curve=-0.45)
text(ax, f(10), 19.5, r'$\times\frac{1}{3}$', 'resultat', 'm')
disc(ax, f(5), 30, 1.3, 'sujet')
disc(ax, f(15), 30, 1.3, 'fixe')
text(ax, f(5), 38, 'départ', 'sujet', 's')
text(ax, f(5), 5, 'retour au départ', 'resultat', 's')
save(fig, '33-087')
