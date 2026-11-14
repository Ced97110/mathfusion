import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 44, 82, r'suite normale de $G$ jusqu’à $\{e\}$', 'sujet', 'm', weight='bold')
labs = [r'$G_1=G$ : 24', r'$G_2$ : 12', r'$G_3$ : 4', r'$G_4=\{e\}$ : 1']
arrs = [r'$G_2$ normal dans $G_1$', r'$G_3$ normal dans $G_2$', r'$G_4$ normal dans $G_3$']
for i, lab in enumerate(labs):
    y = 62 - 19 * i
    box(ax, 6, y, 34, 11, 'sujet', label=lab, size='s')
    if i < 3:
        arrow(ax, (23, y - 0.5), (23, y - 7.5), 'varie')
        text(ax, 46, y - 4, arrs[i], 'varie', 's', ha='left')
save(fig, '64-026')
