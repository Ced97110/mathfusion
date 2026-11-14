import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(72)
cen, pos = venn(ax, 44, 38)
word = '0011011'
for k, (x, y) in pos.items():
    b = word[k - 1]
    if b == '1':
        disc(ax, x, y, 3.3, 'fixe')
    text(ax, x, y, b, 'encre', 'l', weight='bold' if b == '1' else 'normal')
disc(ax, pos[6][0], pos[6][1], 4.6, 'limite', fill=False, lw=1.6)
lab = venn_labels(cen)
for n, role, s in (('A', 'sujet', 'A : 3 (impair)'), ('B', 'varie', 'B : 3 (impair)'), ('C', 'resultat', 'C : 2 (pair)')):
    text(ax, *lab[n], s, role, 'm', weight='bold')
text(ax, 44, 4, 'mot reçu 0011011', 'encre', 'm')
save(fig, '68-143')
