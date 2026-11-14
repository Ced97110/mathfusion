import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(92)
leaf = [14 + 9.5 * i for i in range(8)]
l2 = [(leaf[2 * k] + leaf[2 * k + 1]) / 2 for k in range(4)]
l1 = [(l2[0] + l2[1]) / 2, (l2[2] + l2[3]) / 2]
root = (l1[0] + l1[1]) / 2
Y = [86, 68, 50]
def branch(p, q, taken):
    line(ax, [p, q], 'varie' if taken else 'fixe', lw=1.5 if taken else 0.9)
for j in range(2):
    branch((root, Y[0]), (l1[j], Y[1]), j == 1)
for k in range(4):
    branch((l1[k // 2], Y[1]), (l2[k], Y[2]), k % 2 == 1)
for i in range(8):
    branch((l2[i // 2], Y[2]), (leaf[i], 31), i % 2 == 1)
disc(ax, root, Y[0], 1.6, 'fixe')
for x in l1: disc(ax, x, Y[1], 1.6, 'fixe')
for x in l2: disc(ax, x, Y[2], 1.6, 'fixe')
for i in range(8):
    v = (2 if i & 4 else 1) * (3 if i & 2 else 1) * (5 if i & 1 else 1)
    box(ax, leaf[i] - 4.2, 22, 8.4, 9, 'sujet', label=str(v))
for n, y in zip(('2', '3', '5'), (77, 59, 41)):
    text(ax, 3, y, n + ' ?', 'encre', 's', ha='left')
text(ax, 22, 15, 'trait orange : pris', 'varie', 's')
text(ax, 62, 15, 'trait gris : non pris', 'fixe', 's')
text(ax, 44, 7, r'$2\times2\times2=8$', 'resultat', 'l')
save(fig, '80-339')
