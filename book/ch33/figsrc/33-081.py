import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(64)
box(ax, 5, 48, 36, 11, 'sujet', label=r'$\tan^{-1}\,x$', size='l')
text(ax, 47, 53.5, '=', 'encre', 'l')
box(ax, 53, 48, 30, 11, 'autre', label=r'$\arctan\,x$', size='l')
text(ax, 23, 44, 'tangente moins un de x', 'sujet', 's')
text(ax, 68, 44, 'arctangente de x', 'autre', 's')
o = (26, 22)
line(ax, [(o[0]-14, o[1]), (o[0]+30, o[1])], 'fixe')
for sg, lab in ((1, r'$x=1$ : 45°'), (-1, r'$x=-1$ : $-45$°')):
    q = (o[0]+15, o[1]+sg*15)
    line(ax, [o, q], 'sujet', lw=1.3)
    arcp(ax, o, 9, 0, 45*sg) if sg > 0 else arcp(ax, o, 9, -45, 0)
    text(ax, q[0]+2, q[1], lab, 'resultat', 's', ha='left')
save(fig, '33-081')
