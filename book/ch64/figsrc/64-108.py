import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 21, 42, r'$A_4$ : 12 éléments', 'sujet', 's')
for r in range(3):
    for c in range(4):
        disc(ax, 21 + (c - 1.5) * 5, 32 - r * 5, 1.5, 'autre' if r == 0 else 'sujet')
box(ax, 21 - 9.5, 32 - 3, 19, 6, 'autre', fill=False, dash=True, r=1.0)
text(ax, 21, 13, r'$V$ : 4 éléments, normal', 'autre', 's')
text(ax, 21, 5, r'$n=4$ : $A_4$ non simple', 'limite', 's')
text(ax, 65, 42, r'$A_5$ : 60 éléments', 'sujet', 's')
for r in range(6):
    for c in range(10):
        disc(ax, 65 + (c - 4.5) * 3.8, 34 - r * 3.8, 1.1, 'sujet')
text(ax, 65, 11, r'seuls $\{e\}$ et $A_5$ normaux', 'sujet', 's')
text(ax, 65, 5, r'$n=5$ : simple', 'resultat', 's')
save(fig, '64-108')
