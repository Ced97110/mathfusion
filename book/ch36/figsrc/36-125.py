import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(84)
s = 5.5; x0 = 20; y = 52
xl, xr = x0, x0 + 8*s
line(ax, [(xl, y), (xr, y)], 'fixe', lw=1.5)
disc(ax, xl, y, 2*s, 'sujet', fill=False); disc(ax, xr, y, 3*s, 'autre', fill=False)
line(ax, [(xl, y), (xl + 2*s, y)], 'sujet', lw=1.2); line(ax, [(xr, y), (xr - 3*s, y)], 'autre', lw=1.2)
text(ax, xl + s, y + 3, '2', 'sujet', 's'); text(ax, xr - 1.5*s, y + 3, '3', 'autre', 's')
text(ax, (xl + xr) / 2 + 4, y - 3, '8', 'fixe', 's')
arrow(ax, (xl + 2*s + 1, y - 9), (xr - 3*s - 1, y - 9), 'limite', both=True)
text(ax, (xl + 2*s + xr - 3*s) / 2, y - 13, 'ne se touchent pas', 'limite', 's')
text(ax, 44, 20, r'$\cos A=\dfrac{4+9-64}{12}=-4{,}25$', 'encre', 'm')
text(ax, 44, 9, r'$-4{,}25<-1$ : impossible', 'limite', 'm')
save(fig, '36-125')
