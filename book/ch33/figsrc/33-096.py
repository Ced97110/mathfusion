import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(46)
x0, x1, y = 6, 70, 14
f = numberline(ax, x0, x1, y, -1, 3, step=1, labels=False)
for v in range(-1, 4):
    text(ax, f(v), y - 4, str(v).replace('-', '−'), 'fixe', 's')
box(ax, f(-1), 21, f(1) - f(-1), 9, 'fixe', label='sinus, cosinus', size='s', dash=True)
disc(ax, f(1.0909), y, 1.5, 'resultat')
text(ax, 52, 26, 'rapport 1,0909', 'resultat', 's', ha='left')
arrow(ax, (54, 24), (f(1.0909)+0.8, y+1.8), 'resultat')
box(ax, 14, 36, 60, 9, 'resultat', label='arctan accepte tout nombre', size='s')
save(fig, '33-096')
