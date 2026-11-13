import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
p, gx, gy = 11, 24, 12
for i in range(1, 4):
    for j in range(1, 4):
        hit = (i, j) == (2, 3)
        box(ax, gx + (j - 1) * p, gy + (3 - i) * p, p - 1, p - 1, 'varie' if hit else 'fixe', label='1' if hit else '0', weight='bold' if hit else 'normal')
text(ax, gx + 2.5 * p - 0.5, 50, r'colonne $j=3$', 'varie', 's')
text(ax, 10, gy + 1.5 * p - 0.5, r'ligne $i=2$', 'varie', 's')
text(ax, 73, 36, r'$e_{23}$', 'varie', 'xl'); text(ax, 73, 26, '« $e$ deux trois »', 'encre', 's')
save(fig, '73-123')
