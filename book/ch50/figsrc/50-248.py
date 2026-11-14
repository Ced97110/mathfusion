import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
for r in range(6):
    for c in range(10): box(ax, 20 + 4.8 * c, 62 + 4.8 * r, 4, 4, 'sujet', r=0.2, lw=0.5)
text(ax, 44, 94, r'$A_5$ : 60 éléments', 'sujet', 'm', weight='bold')
arrow(ax, (44, 60), (44, 52), 'fixe')
box(ax, 18, 32, 52, 19, 'limite', fill=False, dash=True)
text(ax, 44, 45, 'aucun sous-groupe', 'limite', 's'); text(ax, 44, 38, 'normal intermédiaire', 'limite', 's')
arrow(ax, (44, 30), (44, 20), 'fixe')
box(ax, 42, 14, 4, 4, 'fixe', r=0.2, lw=0.5)
text(ax, 50, 16, 'identité : 1', 'fixe', 's', ha='left')
text(ax, 44, 5, 'non résoluble', 'limite', 'm', weight='bold')
save(fig, '50-248')
