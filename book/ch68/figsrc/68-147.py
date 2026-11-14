import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(74)
cen, pos = venn(ax, 44, 40, lw=(1.8, 1.8, 0.7))
disc(ax, pos[6][0], pos[6][1], 5.0, 'varie')
for k, (x, y) in pos.items():
    text(ax, x, y, str(k), 'encre' if k == 6 else 'fixe', 'l', weight='bold' if k == 6 else 'normal')
lab = venn_labels(cen)
for n, role, s in (('A', 'sujet', 'A impair : 4'), ('B', 'varie', 'B impair : 2'), ('C', 'resultat', 'C pair : ignoré')):
    text(ax, *lab[n], s, role, 'm', weight='bold')
text(ax, 44, 4, '4 + 2 = 6 : bit 6 faux', 'resultat', 'l', weight='bold')
save(fig, '68-147')
