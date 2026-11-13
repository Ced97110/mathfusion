import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

M = [[2, 0], [0, 1]]
det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
assert det == 2 and math.gcd(det, 26) == 2
assert (2 * 0) % 26 == 0 and (2 * 13) % 26 == 0 and 2 * 13 == 26

fig, ax = canvas(80)
for i in range(2):
    for j in range(2):
        box(ax, 3 + j * 9.8, 62 - i * 9.8, 9, 9, 'sujet', label=str(M[i][j]))
text(ax, 26, 70, r'déterminant : $2 \times 1 - 0 \times 0 = 2$', 'sujet', 's', ha='left')
text(ax, 26, 63, '2 n’est pas premier avec 26', 'limite', 's', ha='left')
box(ax, 3, 36, 20, 12, 'sujet', label='AA\n(0, 0)', size='s')
box(ax, 3, 10, 20, 12, 'autre', label='NA\n(13, 0)', size='s')
box(ax, 64, 10, 20, 38, 'limite', label='AA\n(0, 0)', size='s')
arrow(ax, (24, 42), (63, 42), 'varie')
arrow(ax, (24, 16), (63, 16), 'varie')
text(ax, 43.5, 46, r'$2 \times 0 = 0$', 'varie', 's')
text(ax, 43.5, 20, r'$2 \times 13 = 26 \to 0$', 'varie', 's')
save(fig, '53-071')
