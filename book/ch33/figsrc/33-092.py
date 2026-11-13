import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(60)
c = (28, 30); R = 22
ax.add_patch(Circle(c, R, ec=COL['fixe'], fc='none', lw=1.0, zorder=2))
line(ax, [(c[0]-R-3, c[1]), (c[0]+R+3, c[1])], 'fixe'); line(ax, [(c[0], c[1]-R-2), (c[0], c[1]+R+2)], 'fixe')
P1, P2 = pol(c, R, 30), pol(c, R, 150)
line(ax, [P1, P2], 'varie', lw=1.0, dash=True)
line(ax, [c, P1], 'sujet', lw=1.4); line(ax, [c, P2], 'resultat', lw=1.4)
disc(ax, P1[0], P1[1], 1.3, 'sujet'); disc(ax, P2[0], P2[1], 1.3, 'resultat')
text(ax, P1[0]+2, P1[1]+2.5, '30°', 'sujet', 's', ha='left')
text(ax, P2[0]-2, P2[1]+2.5, '150°', 'resultat', 's', ha='right')
text(ax, c[0], c[1]+R*0.5+2.5, '0,5', 'varie', 's')
arcp(ax, c, 7, 0, 30, 'sujet'); arcp(ax, c, 11, 0, 150, 'resultat')
box(ax, 56, 38, 30, 9, 'resultat', label=r'$180°-30°=150°$', size='s')
box(ax, 56, 24, 30, 9, 'fixe', label=r'$30°+360°=390°$', size='s')
box(ax, 56, 10, 30, 9, 'fixe', label=r'$150°+360°=510°$', size='s')
save(fig, '33-092')
