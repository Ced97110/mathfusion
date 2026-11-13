import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
gA = [(10, '1'), (22, '3'), (34, '5'), (46, '8')]
gB = [(66, '2'), (78, '6')]
box(ax, 3, 42, 50, 14, 'fixe', fill=False, dash=True)
box(ax, 58, 42, 27, 14, 'fixe', fill=False, dash=True)
for x, n in gA + gB:
    disc(ax, x, 49, 4.5, 'sujet', label=n)
text(ax, 28, 61, 'cycle de longueur 4', 'sujet', 's')
text(ax, 71.5, 61, 'longueur 2', 'sujet', 's')
sA = [10, 25, 40]
for x in sA:
    box(ax, x - 5.5, 24, 11, 7, 'varie')
box(ax, 66, 24, 11, 7, 'varie')
arrow(ax, (28, 41), (28, 33), 'varie')
arrow(ax, (71.5, 41), (71.5, 33), 'varie')
brace(ax, 4.5, 45.5, 23, 'varie', label='3 échanges')
brace(ax, 66, 77, 23, 'varie', label='1 échange')
box(ax, 22, 2, 44, 9, 'resultat', label='4 échanges en tout')
save(fig, '46-200')
