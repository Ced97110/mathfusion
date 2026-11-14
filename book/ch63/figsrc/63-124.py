import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(78)
text(ax, 44, 72, r'$F\subseteq K\subseteq E$', 'autre', 'm')
ax.add_patch(Ellipse((44, 38), 84, 56, ec=COL['autre'], fc='none', lw=1.2, zorder=1))
text(ax, 12, 60, r'$\Sigma$', 'autre', 'xl')
box(ax, 20, 44, 24, 10, 'autre', label=r'$F=\mathbb{Q}$', size='s')
box(ax, 48, 44, 24, 10, 'autre', label=r'$E$', size='s')
for i, l in enumerate([r'$\mathbb{Q}(\sqrt{3})$', r'$\mathbb{Q}(\sqrt{2})$', r'$\mathbb{Q}(\sqrt{6})$']):
    box(ax, 11 + i * 25, 24, 22, 10, 'autre', label=l, size='s')
text(ax, 44, 4,r'$\Sigma$ : 5 corps intermédiaires $K$', 'autre', 's')
save(fig, '63-124')
