import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(66)
text(ax, 22, 61, r'$\sin^{2}\,30°$', 'autre', 'l')
text(ax, 66, 61, r'$\sin^{-1}\,0{,}5$', 'sujet', 'l')
box(ax, 8, 20, 28, 28, 'fixe', fill=True)
box(ax, 8, 20, 14, 14, 'autre', label='0,25', size='s')
text(ax, 22, 15, r'$0{,}5\times0{,}5$', 'autre', 's')
text(ax, 22, 8, 'un carré', 'autre', 'm')
o = (50, 26)
line(ax, [o, (o[0]+30, o[1])], 'fixe')
q = pol(o, 28, 30)
line(ax, [o, q], 'sujet', lw=1.4)
arcp(ax, o, 12, 0, 30)
text(ax, 67, 30, '30°', 'resultat', 's')
text(ax, 66, 8, 'un angle', 'sujet', 'm')
save(fig, '33-088')
