import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(74)
ox, oy, u = 30, 12, 3.0
def P(x, y): return (ox + u * x, oy + u * y)
arrow(ax, (ox - 14, oy), (ox + 46, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 4), (ox, oy + 54), 'fixe', lw=0.7)
y0, y1 = -1.5, 14.0
line(ax, [P((3 * y0 - 10) / 8, y0), P((3 * y1 - 10) / 8, y1)], 'autre', lw=1.4)
th = math.atan(8 / 3)
L = 14.5
line(ax, [P(0, 0), P(L * math.cos(th) , L * math.sin(th))], 'sujet', lw=1.4)
ax.add_patch(Arc((ox, oy), 16, 16, theta1=0, theta2=math.degrees(th), color=COL['varie'], lw=1.1, zorder=3))
text(ax, 33, 43,'droite\npente 8/3 ≈ 2,67', 'autre', 's', ha='right')
text(ax, 50, 43, 'demi-droite\nd’angle θ', 'sujet', 's', ha='left')
text(ax, ox + 11, oy + 5.5, r'$\theta\approx 69{,}4^\circ$', 'varie', 's', ha='left')
text(ax, 44, 69, r'$\tan\theta=8/3$ = pente', 'resultat', 'm')
text(ax, 44, 5, 'aucun point à cet angle', 'encre', 's')
save(fig, '40-109')
