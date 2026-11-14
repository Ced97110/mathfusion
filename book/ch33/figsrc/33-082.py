import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(62)
text(ax, 22, 57, 'écriture anglaise', 'sujet', 's')
text(ax, 66, 57, 'écriture du livre', 'autre', 's')
rows = [(r'$\sin^{-1}\,x$', r'$\arcsin\,x$'), (r'$\cos^{-1}\,x$', r'$\arccos\,x$'), (r'$\tan^{-1}\,x$', r'$\arctan\,x$')]
for i, (a, b) in enumerate(rows):
    y = 38 - i * 17
    box(ax, 6, y, 32, 11, 'sujet', label=a, size='l')
    text(ax, 44, y + 5.5, '=', 'encre', 'l')
    box(ax, 50, y, 32, 11, 'autre', label=b, size='l')
save(fig, '33-082')
