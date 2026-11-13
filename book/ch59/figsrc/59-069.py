import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 4, 56, r'$2\mid 10$ : $10=2\times5$', 'resultat', 'm', ha='left')
for i in range(5):
    x = 4 + i * 16.4
    box(ax, x, 40, 14, 9, 'resultat', fill=False)
    for d in (-3, 3):
        disc(ax, x + 7 + d, 44.5, 2.2, 'sujet')
text(ax, 4, 33, r'$4\nmid 10$ : il reste 2', 'limite', 'm', ha='left')
for i in range(2):
    x = 4 + i * 30
    box(ax, x, 16, 28, 9, 'fixe', fill=False)
    for d in range(4):
        disc(ax, x + 5.5 + d * 5.7, 20.5, 2.2, 'sujet')
box(ax, 64, 16, 14, 9, 'limite', fill=False, dash=True)
for d in (-3, 3):
    disc(ax, 71 + d, 20.5, 2.2, 'limite')
text(ax, 71, 10, 'reste', 'limite', 's')
save(fig, '59-069')
