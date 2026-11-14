import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 61, r'$G$ simple : $G^{\prime}$ (groupe dérivé) est normal,' + '\n' + r'donc $G^{\prime}=\{e\}$ ou $G^{\prime}=G$', 'sujet', 's')
box(ax, 7, 38, 30, 10, 'sujet', label=r'$\mathbb{Z}/3$')
box(ax, 51, 38, 30, 10, 'autre', label=r'$A_5$ (60)')
box(ax, 7, 12, 30, 10, 'resultat', label=r'$\{e\}$')
box(ax, 51, 12, 30, 10, 'limite', label=r'$A_5$ (60)')
for x in (22, 66):
    arrow(ax, (x, 38), (x, 22), 'varie')
    text(ax, x + 3, 30, r'$G^{\prime}$', 'varie', 's', ha='left')
text(ax, 22, 5, r'$G^{\prime}=\{e\}$ : abélien, $\mathbb{Z}/p$', 'resultat', 's', weight='bold')
text(ax, 66, 5, r'$G^{\prime}=G$ : pas résoluble', 'limite', 's', weight='bold')
save(fig, '64-084')
