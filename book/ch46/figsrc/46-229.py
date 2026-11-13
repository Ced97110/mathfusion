import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 38, 64, r'$A$', 'sujet', 'xl'); text(ax, 44, 61.5, r'$n$', 'varie', 'm')
arrow(ax, (36, 59), (24, 49), 'sujet'); arrow(ax, (46, 59), (62, 49), 'varie')
text(ax, 22, 45, 'permutations paires', 'sujet', 's'); text(ax, 66, 45, 'nombre de nombres', 'varie', 's')
for y, k, lab in [(26, 3, r'$A_3$ : 3'), (8, 12, r'$A_4$ : 12')]:
    text(ax, 4, y + 7, lab, 'encre', 'm', ha='left')
    for i in range(k): box(ax, 4 + i * 6.6, y - 3, 6, 6, 'sujet', lw=0.6, r=0.4)
save(fig, '46-229')
