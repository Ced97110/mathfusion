import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(56)
text(ax, 44, 52, '(+, +)', 'encre', 'm')
ax.add_patch(Ellipse((20, 30), 14, 24, ec=COL['sujet'], fc=FILL['sujet'], lw=1.3, zorder=2))
ax.add_patch(Circle((68, 30), 12, ec=COL['resultat'], fc=FILL['resultat'], lw=1.3, zorder=2))
arrow(ax, (34, 30), (53, 30), 'varie')
text(ax, 43.5, 36, '$\\times\\frac{1}{4}$ et $\\times\\frac{1}{2}$', 'varie', 's')
text(ax, 20, 13, '$16s^2+4t^2=1$', 'sujet', 's'); text(ax, 68, 13, '$x^2+y^2=1$', 'resultat', 's')
text(ax, 20, 4, 'ellipse', 'sujet', 'm'); text(ax, 68, 4, 'cercle', 'resultat', 'm')
save(fig, '71-191')
