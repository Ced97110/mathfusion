import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arcp(ax, c, r, t1, t2, role="resultat"):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=1.0, zorder=3))
def pol(c, r, deg):
    a = math.radians(deg); return (c[0] + r*math.cos(a), c[1] + r*math.sin(a))
fig, ax = canvas(58)
x0, x1, y = 6, 78, 28
f = lambda v: x0 + (v + 90) / 630 * (x1 - x0)
numberline(ax, x0, x1, y, -90, 540, step=90, labels=False, arrow_right=False)
for v in range(-90, 541, 90):
    text(ax, f(v), y - 4, f'{v}°'.replace('-', '−'), 'fixe', 's')
brace(ax, f(-90), f(90), 41, 'sujet', down=False, label='[−90°, 90°]')
for v in (150, 390, 510):
    disc(ax, f(v), y, 1.4, 'varie'); text(ax, f(v), y + 5, f'{v}°', 'varie', 's')
disc(ax, f(30), y, 2.0, 'resultat'); text(ax, f(30), y + 5, '30°', 'resultat', 's', weight='bold')
disc(ax, 8, 10, 1.6, 'resultat'); text(ax, 11.5, 10, 'valeur principale', 'resultat', 's', ha='left')
disc(ax, 50, 10, 1.4, 'varie'); text(ax, 53.5, 10, 'autres solutions', 'varie', 's', ha='left')
text(ax, 44, 54, 'angles de sinus 0,5', 'encre', 'm')
save(fig, '33-091')
