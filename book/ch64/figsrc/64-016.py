import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$S_4$ = toutes les files de 4', 'sujet', 'm', weight='bold')
for k in range(4):
    cx = 14 + 20 * k
    text(ax, cx, 54, f'place {k + 1}', 'fixe', 's')
    for j in range(4 - k):
        disc(ax, cx, 46 - 6.5 * j, 2.4, 'sujet')
    text(ax, cx, 17, f'{4 - k} choix', 'varie', 's')
text(ax, 44, 8, '4 × 3 × 2 × 1 = 24 files', 'resultat', 'm', weight='bold')
save(fig, '64-016')
