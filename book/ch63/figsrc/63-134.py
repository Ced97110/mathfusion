import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 22, 3, 44, 10, role='fixe', label='deux inégalités')
arrow(ax, (44, 13.8), (44, 21.2), 'varie')
box(ax, 22, 22, 44, 10, role='autre', label='théorème 4.7')
arrow(ax, (44, 32.8), (44, 40.2), 'varie')
box(ax, 14, 41, 60, 12, role='sujet', label='bijection  H ↔ K', weight='bold')
text(ax, 3, 8, 'd’abord', 'encre', 's', ha='left')
tops = [15, 44, 73]
for cx, t in zip(tops, ['ordre', 'tailles', 'normalité']):
    box(ax, cx - 13, 66, 26, 10, role='resultat', label=t)
    arrow(ax, (44 + (cx - 44) * 0.35, 53.8), (cx, 65.2), 'varie')
text(ax, 44, 81, 'ensuite : trois compléments', 'encre', 's')
save(fig, '63-134')
