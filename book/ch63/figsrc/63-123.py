import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(72)
ax.add_patch(Ellipse((44, 36), 84, 56, ec=COL['sujet'], fc='none', lw=1.2, zorder=1))
text(ax, 12, 58, r'$\Gamma$', 'sujet', 'xl')
box(ax, 24, 42, 20, 10, 'sujet', label=r'$\{1\}$', size='s')
box(ax, 48, 42, 20, 10, 'sujet', label=r'$G$', size='s')
for i, l in enumerate([r'$\langle\sigma\rangle$', r'$\langle\tau\rangle$', r'$\langle\sigma\tau\rangle$']):
    box(ax, 11 + i * 25, 22, 22, 10, 'sujet', label=l, size='s')
text(ax, 44, 3,r'$\Gamma$ : 5 sous-groupes de $G$', 'sujet', 's')
save(fig, '63-123')
