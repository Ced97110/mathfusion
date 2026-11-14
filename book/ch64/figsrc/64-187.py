import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$G$ simple et non abélien', 'encre', 'm')
box(ax, 26, 44, 36, 14, 'sujet', label=r'$A_5$ : 60 éléments')
box(ax, 34, 8, 20, 11, 'fixe', label=r'$\{e\}$')
arrow(ax, (44, 43), (44, 20), 'limite', lw=1.3)
text(ax, 47, 31.5, 'seul facteur : $A_5$\nnon abélien', 'limite', 's', ha='left')
text(ax, 41, 31.5, 'aucun\nintermédiaire', 'fixe', 's', ha='right')
save(fig, '64-187')
