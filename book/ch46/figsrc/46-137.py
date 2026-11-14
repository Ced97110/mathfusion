import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(52)
text(ax, 2, 47, 'horloge à 12 heures', 'sujet', 'm', ha='left')
D = [1, 2, 3, 4, 6, 12]
for i, d in enumerate(D):
    cx = 8 + i * 14.4
    box(ax, cx - 5.5, 34, 11, 6, 'varie', label=str(d), size='s', r=0.6)
    arrow(ax, (cx, 34), (cx, 29), 'varie', lw=0.8)
    box(ax, cx - 5.5, 6, 11, 22, 'sujet', r=0.6)
    for j in range(d):
        disc(ax, cx - 2 + (j % 2) * 4 if d > 1 else cx, 25 - (j // 2) * 3.4, 1.0, 'sujet')
text(ax, 2, 43, 'diviseurs positifs : 6', 'varie', 's', ha='left')
text(ax, 2, 2.6, 'sous-groupes : 6, un par diviseur', 'sujet', 's', ha='left')
save(fig, '46-137')
