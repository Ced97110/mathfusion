import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(72)
cen, pos = venn(ax, 44, 38)
for k, (x, y) in pos.items():
    text(ax, x, y, str(k), 'encre', 'l')
lab = venn_labels(cen)
for n, role, s in (('A', 'sujet', 'A : 4, 5, 6, 7'), ('B', 'varie', 'B : 2, 3, 6, 7'), ('C', 'resultat', 'C : 1, 3, 5, 7')):
    text(ax, *lab[n], s, role, 'm', weight='bold')
text(ax, 44, 4, 'règle : un nombre pair de 1', 'encre', 'm')
save(fig, '68-142')
