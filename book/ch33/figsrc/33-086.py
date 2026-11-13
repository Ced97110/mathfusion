import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(46)
rows = [(32, ['5', '15', '5'], [r'$\times 3$', r'$\times\frac{1}{3}$']),
        (6, ['30°', '0,5', '30°'], ['sin', 'arcsin'])]
for y, vals, ops in rows:
    for i, v in enumerate(vals):
        box(ax, 4 + i * 31, y, 18, 10, 'fixe' if i == 1 else 'sujet', label=v, size='l')
    for i, o in enumerate(ops):
        xa = 4 + i * 31 + 18
        arrow(ax, (xa + 1, y + 5), (xa + 12, y + 5), 'varie' if i == 0 else 'resultat', lw=1.2)
        text(ax, xa + 6.5, y + 9.5, o, 'varie' if i == 0 else 'resultat', 's')
save(fig, '33-086')
