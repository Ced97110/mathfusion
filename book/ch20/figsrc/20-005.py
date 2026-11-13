import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
text(ax, 28, 47, 'gâteaux', 'varie', 'm'); text(ax, 57, 47, 'pains au plus', 'sujet', 'm')
for (lab, ng, nb, y) in [('0 gâteau', 0, 6, 34), ('2 gâteaux', 2, 3, 20), ('4 gâteaux', 4, 0, 6)]:
    text(ax, 2, y + 2.3, lab, 'encre', 's', ha='left')
    for i in range(ng): box(ax, 22 + 5 * i, y, 4.5, 4.5, 'varie', r=0.6)
    for i in range(6):
        if i < nb: box(ax, 44 + 5 * i, y, 4.5, 4.5, 'sujet', r=0.6)
        else: box(ax, 44 + 5 * i, y, 4.5, 4.5, 'fixe', fill=False, dash=True, lw=0.6, r=0.6)
    text(ax, 77, y + 2.3, str(nb), 'sujet', 'l', weight='bold')
save(fig, '20-005')
