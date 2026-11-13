import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, '30 cm, deux rois', 'encre', 'm', weight='bold')
box(ax, 6, 62, 60, 7, 'fixe', label='ruban 30 cm', size='s')
text(ax, 6, 56, 'roi 1 : pouce 2,5 cm', 'varie', 's', ha='left')
for i in range(12): box(ax, 6 + i * 5, 48, 5, 6, 'varie', lw=0.6, r=0.3)
text(ax, 72, 51, '12 pouces', 'varie', 's', ha='left')
text(ax, 6, 42, 'roi 2 : pouce 3 cm', 'autre', 's', ha='left')
for i in range(10): box(ax, 6 + i * 6, 34, 6, 6, 'autre', lw=0.6, r=0.3)
text(ax, 69, 37, '10 pouces', 'autre', 's', ha='left')
line(ax, [(2, 28), (86, 28)], 'fixe', dash=True)
for i, n in enumerate(['accessible', 'invariable', 'reproductible']):
    box(ax, 3 + i * 28.5, 8, 26, 12, 'limite', label=n + '\n' + r'$\times$', size='s')
save(fig, '11-020')
