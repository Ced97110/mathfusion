import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(64)
x0, x1 = 10, 78
f = numberline(ax, x0, x1, 32, 0, 0.1, step=0.02, arrow_right=False)
xv = f(1/12)
line(ax, [(xv, 33), (xv, 46)], 'resultat', lw=1.2, dash=True)
line(ax, [(xv, 23.2), (xv, 18)], 'resultat', lw=1.2, dash=True)
disc(ax, xv, 32, 1.3, 'resultat')
box(ax, xv-15, 47, 30, 10, 'sujet', label=r'$\tan 4{,}76°$', size='m')
box(ax, xv-15, 7, 30, 10, 'autre', label=r'$1\div12$', size='m')
text(ax, xv+2, 40, '≈ 0,0833', 'resultat', 's', ha='left')
text(ax, xv-2, 24, 'même nombre', 'resultat', 's', ha='right')
save(fig, '33-094')
