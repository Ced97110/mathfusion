import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 16, 57, 'ligne de 2 : le calcul', 'encre', 's'); text(ax, 62, 57, 'les trois lignes', 'encre', 's')
for i in range(4):
    y = 42 - i * 10.5
    box(ax, 2, y, 28, 8.5, 'limite' if i in (0, 2) else 'fixe', label=r'$2\times%d=%d$' % (i, (2 * i) % 4))
rows = [('1', '0 1 2 3', 'resultat'), ('2', '0 2 0 2', 'limite'), ('3', '0 3 2 1', 'resultat')]
for k, (a, s, r) in enumerate(rows):
    box(ax, 38, 40 - k * 14, 48, 11, r, label='ligne de %s : %s' % (a, s))
text(ax, 16, 7, '0 et 2 : même image 0', 'limite', 's')
save(fig, '45-086')
