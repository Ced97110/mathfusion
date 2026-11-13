import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 4, 56, 'identité : 1', 'sujet', 's', ha='left'); text(ax, 22, 56, 'doubles échanges : 3', 'sujet', 's', ha='left')
box(ax, 4, 44, 10, 8, 'sujet')
for i, l in enumerate(['(1 2)(3 4)', '(1 3)(2 4)', '(1 4)(2 3)']): box(ax, 22 + i * 21, 44, 19, 8, 'sujet', label=l, size='s')
text(ax, 4, 36, 'cycles de longueur 3 : 8', 'sujet', 's', ha='left')
for i in range(8): box(ax, 4 + i * 10.3, 24, 9, 8, 'sujet')
text(ax, 44, 10, '1 + 3 + 8 = 12', 'resultat', 'l')
save(fig, '46-237')
