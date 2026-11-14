import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
words = ['0000', '0011', '0101', '0110', '1001', '1010', '1100', '1111']
text(ax, 22, 46, 'liste des 8 mots', 'fixe', 's')
for i, w in enumerate(words):
    box(ax, 2 + 11 * (i % 4), 28 - 11 * (i // 4) + 5, 10.5, 8, 'fixe', label=w, size='s')
arrow(ax, (47, 29), (55, 29), 'varie', both=True)
text(ax, 71, 46, r'$H$ : $m=1$, $n=4$', 'sujet', 's')
for c in range(4):
    box(ax, 55 + 8 * c, 25, 8, 8, 'sujet', label='1')
save(fig, '68-108')
