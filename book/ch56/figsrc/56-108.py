import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(64)
ax.add_patch(Ellipse((44, 34), 76, 50, ec=COL['autre'], fc=FILL['autre'], lw=0.9, zorder=1))
ax.add_patch(Ellipse((32, 34), 44, 30, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=1.5))
text(ax, 44, 54, 'anneaux noethériens', 'autre', 's')
text(ax, 32, 43.5, 'anneaux principaux', 'sujet', 's')
disc(ax, 24, 32, 4.5, 'resultat', label='ℤ')
text(ax, 44, 3, 'un seul générateur ⇒ stable', 'fixe', 's')
save(fig, '56-108')
