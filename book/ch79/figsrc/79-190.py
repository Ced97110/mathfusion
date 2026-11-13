import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Circle
fig, ax = canvas(66)
ax.add_patch(Circle((24, 34), 17, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=1, alpha=0.8))
ax.add_patch(Circle((44, 34), 17, ec=COL['autre'], fc=FILL['autre'], lw=1.0, zorder=1, alpha=0.8))
ov = Circle((44, 34), 17, ec=COL['resultat'], fc=FILL['resultat'], lw=0, zorder=1.5); ax.add_patch(ov)
ov.set_clip_path(Circle((24, 34), 17, transform=ax.transData))
text(ax, 15, 34, '1', 'sujet', 'l'); text(ax, 34, 40, '2', 'resultat', 'l'); text(ax, 34, 28, '3', 'resultat', 'l'); text(ax, 53, 34, '4', 'autre', 'l')
text(ax, 12, 56, r'$A$', 'sujet', 'l'); text(ax, 56, 56, r'$B$', 'autre', 'l')
text(ax, 74, 52, r'$|A\cup B|=4$', 'fixe', 's'); text(ax, 74, 43, r'$|A\cap B|=2$', 'resultat', 's')
text(ax, 74, 31, r'$|A|=3$', 'sujet', 's'); text(ax, 74, 22, r'$|B|=3$', 'autre', 's')
text(ax, 44, 6, r'$4+2=3+3$', 'encre', 'l', weight='bold')
save(fig, '79-190')
