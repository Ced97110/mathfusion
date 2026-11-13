import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(64)
text(ax, 20, 50, '(2, 3)', 'sujet', 'l')
text(ax, 44, 50, r'$\sim$', 'varie', 'l')
text(ax, 68, 50, '(4, 6)', 'autre', 'l')
text(ax, 44, 59, 'se lit « est équivalent à »', 'varie', 's')
ax.add_patch(Ellipse((44, 28), 70, 24, ec=COL['resultat'], fc=FILL['resultat'], lw=0.9, zorder=1))
text(ax, 26, 28, '(2, 3)', 'sujet', 'm')
text(ax, 62, 28, '(4, 6)', 'autre', 'm')
text(ax, 44, 28, r'$\sim$', 'varie', 'm')
text(ax, 44, 10, 'même groupe, pas identiques', 'resultat', 's')
arrow(ax, (44, 45), (44, 37), 'varie')
save(fig, '54-036')
