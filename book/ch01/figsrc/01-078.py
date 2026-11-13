import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
NB = ' '
fig, ax = canvas(78)
arrow(ax, (8, 66), (84, 66), 'autre')
text(ax, 46, 72, 'dire : depuis la gauche', 'autre', 's', weight='bold')
for x, t in ((16, 'quatre mille'), (36, 'trois cent'), (66, 'vingt-neuf')):
    text(ax, x, 56, t, 'autre', 's')
for i, d in enumerate(['4', '3', '2', '9']):
    box(ax, 8 + 20 * i, 36, 16, 14, 'sujet', label=d, size='l', weight='bold')
for i, v in enumerate(['1' + NB + '000', '100', '10', '1']):
    text(ax, 16 + 20 * i, 29, v, 'fixe', 'm')
ax.add_patch(Circle((84, 19), 1.2, ec=COL['varie'], fc=COL['varie'], lw=0.8, zorder=4))
arrow(ax, (83, 19), (8, 19), 'varie')
text(ax, 46, 11, 'valeur : depuis la droite', 'varie', 's', weight='bold')
save(fig, '01-078')
