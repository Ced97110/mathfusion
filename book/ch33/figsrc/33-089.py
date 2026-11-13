import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(68)
box(ax, 28, 56, 32, 10, 'sujet', label=r'$\sin^{-1}\,0{,}5$', size='l')
arrow(ax, (38, 55), (21, 43), 'fixe'); arrow(ax, (50, 55), (67, 43), 'fixe')
text(ax, 44, 49.5, 'deux lectures', 'encre', 's')
box(ax, 4, 33, 34, 9, 'resultat', label='voulu : angle 30°', size='s')
box(ax, 50, 33, 34, 9, 'limite', label='lu : 1/0,5 = 2', size='s')
box(ax, 4, 6, 34, 10, 'autre', label=r'$\arcsin\,0{,}5$', size='l')
arrow(ax, (39, 11), (49, 11), 'fixe')
box(ax, 50, 6, 34, 10, 'resultat', label='30° seulement', size='s')
text(ax, 44, 22, 'une seule lecture', 'encre', 's')
save(fig, '33-089')
