import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(56)
x0, x1 = 12, 76
f = lambda v: x0 + v * (x1 - x0)
text(ax, 44, 51, r'$1/\sin 30° = 1/0{,}5 = 2$', 'sujet', 'l')
box(ax, f(0), 34, x1 - x0, 7, 'fixe', label='1', size='m')
for i in range(2):
    box(ax, f(i/2), 22, (x1 - x0)/2, 7, 'sujet', label='0,5', size='m')
text(ax, 44, 17, 'dans 1, il y a 2 fois 0,5', 'encre', 's')
box(ax, 22, 3, 44, 9, 'resultat', label='2 : la cosécante de 30°', size='s')
save(fig, '33-085')
