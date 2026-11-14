import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(78)
cen, pos = venn(ax, 44, 44, lw=(1.8, 1.8, 0.7))
disc(ax, pos[6][0], pos[6][1], 5.0, 'varie')
for k, (x, y) in pos.items():
    text(ax, x, y, str(k), 'encre' if k == 6 else 'fixe', 'l', weight='bold' if k == 6 else 'normal')
lab = venn_labels(cen)
for n, role in (('A', 'sujet'), ('B', 'varie'), ('C', 'resultat')):
    text(ax, *lab[n], n, role, 'xl', weight='bold')
for x, role, s in ((4, 'sujet', 'dans A'), (32, 'varie', 'dans B'), (60, 'fixe', 'hors de C')):
    box(ax, x, 2, 24, 9, role, label=s)
save(fig, '68-146')
