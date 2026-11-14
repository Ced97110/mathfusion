import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(66)
# left: galoisian case, F and Inv(Gal) are the same set
ax.add_patch(Ellipse((22, 30), 34, 24, ec=COL['resultat'], fc=FILL['resultat'], lw=1.2, zorder=1))
ax.add_patch(Ellipse((22, 30), 29, 19, ec=COL['sujet'], fc='none', lw=0.9, ls='--', zorder=1.2))
text(ax, 22, 33, r'$F=\mathbb{Q}$', 'sujet', 's')
text(ax, 22, 27, r'$\mathrm{Inv}(\mathrm{Gal})$', 'resultat', 's')
text(ax, 22, 56, r'$\mathbb{Q}(\sqrt{2})/\mathbb{Q}$', 'sujet', 'm')
text(ax, 22, 8, r'$F=\mathrm{Inv}(\mathrm{Gal})$', 'resultat', 's')
# right: non galoisian case, F strictly inside Inv(Gal)
ax.add_patch(Ellipse((66, 30), 34, 24, ec=COL['limite'], fc=FILL['limite'], lw=1.2, zorder=1))
ax.add_patch(Ellipse((60, 29), 12, 9, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=1.2))
text(ax, 60, 29, r'$\mathbb{Q}$', 'sujet', 's')
text(ax, 74, 35, r'$\mathbb{Q}(r)$', 'limite', 's')
text(ax, 66, 56, r'$\mathbb{Q}(r)/\mathbb{Q}$', 'sujet', 'm')
text(ax, 66, 8, r'$F\neq\mathrm{Inv}(\mathrm{Gal})$', 'limite', 's')
save(fig, '63-104')
