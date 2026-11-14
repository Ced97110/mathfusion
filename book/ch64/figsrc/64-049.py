import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
roles = ['fixe', 'sujet', 'autre']
cs = 8.0
def table(x0, y0):
    for i in range(3):
        for j in range(3):
            box(ax, x0 + j * cs, y0 - i * cs, cs, cs, roles[(i + j) % 3], r=0.4, lw=0.5)
table(5, 40)
table(59, 40)
text(ax, 17, 55, r'$\mathbb{Z}/3$ : horloge', 'encre', 's')
text(ax, 71, 55, r'$A_3$ : rotations', 'encre', 's')
text(ax, 44, 36, r'$\cong$', 'varie', 'xl', weight='bold')
text(ax, 44, 28, 'renommer', 'varie', 's')
for k, (lab, role) in enumerate([('0 ↔ ne rien faire', 'fixe'), ('1 ↔ un tiers de tour', 'sujet'), ('2 ↔ deux tiers de tour', 'autre')]):
    y = 14 - k * 5.5 + 5
    box(ax, 12, y - 1.6, 4, 3.2, role, r=0.3, lw=0.5)
    text(ax, 19, y, lab, role if role != 'fixe' else 'encre', 's', ha='left')
save(fig, '64-049')
