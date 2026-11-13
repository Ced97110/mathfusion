import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(52)
k = 6.0
def panel(ax0, role_gf):
    hx = ax0 + 5 * k; y0 = 12
    line(ax, [(ax0, y0), (hx, y0)], 'fixe', 1.4)
    line(ax, [(hx, y0), (hx, y0 + 2 * k)], 'sujet', 1.6)
    line(ax, [(hx - 1.8, y0), (hx - 1.8, y0 + 1.8), (hx, y0 + 1.8)], 'encre', 0.8)
    return hx, y0
# gauche : G au-dessus de H, perpendiculaire
hx, y0 = panel(4, 'resultat')
line(ax, [(4, y0), (hx, y0 + 2 * k)], 'resultat', 1.4)
text(ax, 4, y0 - 4, 'A', 'fixe'); text(ax, hx, y0 - 4, 'H', 'fixe'); text(ax, hx + 1, y0 + 2 * k + 3.5, 'G', 'sujet')
text(ax, 20, 40, r'$GH\perp$ sol : angle droit', 'resultat', 's')
# droite : G joint à F, point du sol qui n'est pas le pied
ox = 50
hx2 = ox + 3.2 * k; y1 = 12
line(ax, [(ox, y1), (hx2, y1)], 'fixe', 1.4)
line(ax, [(hx2, y1), (hx2, y1 + 2 * k)], 'sujet', 1.0, dash=True)
fx = hx2 - 1 * k
line(ax, [(fx, y1), (hx2, y1 + 2 * k)], 'limite', 1.6)
ax.add_patch(Arc((fx, y1), 8, 8, theta1=0, theta2=116.6, color=COL['limite'], lw=0.9, zorder=3))
text(ax, ox, y1 - 4, 'A', 'fixe'); text(ax, fx - 1, y1 - 4, 'F', 'limite'); text(ax, hx2 + 1.5, y1 - 4, 'H', 'fixe')
text(ax, hx2 + 1, y1 + 2 * k + 3.5, 'G', 'sujet')
text(ax, hx2 + 3, y1 + 8, '116,6°', 'limite', 's', ha='left')
text(ax, 66, 40, 'F n’est pas le pied :', 'limite', 's')
text(ax, 66, 35, 'pas d’angle droit', 'limite', 's')
line(ax, [(44, 5), (44, 45)], 'fixe', 0.6, dash=True)
save(fig, '27-039')
