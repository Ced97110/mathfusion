import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(66)
text(ax, 21, 61, 'un angle', 'sujet', 'm')
text(ax, 67, 61, 'un rapport', 'autre', 'm')
box(ax, 4, 44, 34, 11, 'sujet', label=r'$\sin^{-1}\,0{,}5$', size='l')
box(ax, 50, 44, 34, 11, 'autre', label=r'$1/\sin 30°$', size='l')
arrow(ax, (21, 43), (21, 26), 'varie'); arrow(ax, (67, 43), (67, 26), 'varie')
text(ax, 24, 35, "l'angle de sinus 0,5", 'encre', 's', ha='left')
text(ax, 70, 35, r'$1\div0{,}5$', 'encre', 's', ha='left')
box(ax, 8, 12, 26, 12, 'resultat', label='30°', size='l')
box(ax, 54, 12, 26, 12, 'autre', label='2', size='l')
text(ax, 44, 18, r'$\neq$', 'encre', 'xl')
save(fig, '33-083')
