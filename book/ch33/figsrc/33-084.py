import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(70)
c = (28, 33); R = 22
ax.add_patch(Arc(c, 2*R, 2*R, theta1=-90, theta2=90, ec=COL['fixe'], lw=1.0, zorder=2))
line(ax, [(c[0]-4, c[1]), (c[0]+R+4, c[1])], 'fixe'); line(ax, [(c[0], c[1]-R-1), (c[0], c[1]+R+1)], 'fixe')
P = pol(c, R, 30)
line(ax, [c, P], 'sujet', lw=1.4)
line(ax, [P, (P[0], c[1])], 'varie', lw=1.4, dash=True)
disc(ax, P[0], P[1], 1.3, 'sujet')
arcp(ax, c, 9, 0, 30)
text(ax, c[0]+12.5, c[1]+3.2, '30°', 'resultat', 's')
text(ax, P[0]+2, c[1]+P[1]/ P[1]*0 + (P[1]-c[1])/2, '0,5', 'varie', 's', ha='left')
text(ax, c[0]-2, c[1]+R+1.5, '90°', 'fixe', 's', ha='right')
text(ax, c[0]-2, c[1]-R-1.5, '−90°', 'fixe', 's', ha='right')
text(ax, 44, 66, r'$\sin^{-1}\,0{,}5=30$°', 'sujet', 'l')
save(fig, '33-084')
