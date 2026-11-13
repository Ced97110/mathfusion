import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 17, 47, 'nombres', 'sujet', 's'); text(ax, 71, 47, 'rotations', 'autre', 's')
arrow(ax, (17, 57), (71, 57), 'varie', lw=1.6)
text(ax, 44, 62, r'$\eta$', 'varie', 'xl')
for i in range(4):
    y = 3 + 11 * i
    box(ax, 10, y, 14, 8, 'sujet', label=str(3 - i))
    box(ax, 64, y, 14, 8, 'autre', label=r'$r_%d$' % (3 - i))
    arrow(ax, (25, y + 4), (63, y + 4), 'fixe', lw=0.6)
save(fig, '45-017')
