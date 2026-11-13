import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# row 1: without the zero
text(ax, 2, 79, 'sans le 0', 'fixe', 's', ha='left')
box(ax, 14, 62, 20, 12, 'fixe', fill=False, dash=True)
text(ax, 38.5, 67, ',', 'varie', 'l', weight='bold')
box(ax, 43, 62, 20, 12, 'sujet', label='7', size='l')
text(ax, 70, 67, 'virgule seule ?', 'limite', 's', ha='left')
# row 2: with the zero
text(ax, 2, 55, 'avec le 0', 'fixe', 's', ha='left')
text(ax, 24, 50, 'unités', 'fixe', 's'); text(ax, 53, 50, 'dixièmes', 'sujet', 's')
box(ax, 14, 33, 20, 12, 'fixe', label='0', size='l')
text(ax, 38.5, 38, ',', 'varie', 'l', weight='bold')
box(ax, 43, 33, 20, 12, 'sujet', label='7', size='l')
text(ax, 24, 29, '0 entier', 'fixe', 's')
# ruler
for i in range(10):
    ax.add_patch(Rectangle((14 + 6 * i, 12), 6, 8, ec=COL['sujet'], fc=FILL['sujet'] if i < 7 else FILL['fixe'], lw=0.6, zorder=2))
text(ax, 38, 24, '1 mètre : 7 parts sur 10', 'sujet', 's')
text(ax, 44, 6, '0,7 m = 7 dixièmes de mètre', 'sujet', 's')
save(fig, '08-034')
