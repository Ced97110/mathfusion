import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def row(y, n, role, lab):
    text(ax, 2, y + 12.5, lab, role, 's', ha='left')
    for i in range(n): box(ax, 4 + i * 11, y, 11, 9, role, r=0.5)
row(44, 6, 'sujet', 'ouvrier 1 : 6 h pour la dalle'); row(24, 4, 'autre', 'ouvrier 2 : 4 h pour la dalle')
text(ax, 2, 18.5, 'les deux ensemble', 'varie', 's', ha='left')
box(ax, 4, 4, 33, 9, 'varie', dash=True, label='? heures', size='m')
text(ax, 55, 8.5, 'la même dalle', 'fixe', 's')
save(fig, '21-005')
