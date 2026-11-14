import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(72)
cen, pos = venn(ax, 44, 38)
disc(ax, pos[6][0], pos[6][1], 5.0, 'varie')
for k, (x, y) in pos.items():
    text(ax, x, y, f'{k}\n{k:03b}', 'encre', 's', weight='bold' if k == 6 else 'normal')
lab = venn_labels(cen)
for n, role, s in (('A', 'sujet', 'A : vaut 4'), ('B', 'varie', 'B : vaut 2'), ('C', 'resultat', 'C : vaut 1')):
    text(ax, *lab[n], s, role, 'm', weight='bold')
text(ax, 44, 4, '6 = 4 + 2 : dans A et B', 'varie', 'm')
save(fig, '68-144')
