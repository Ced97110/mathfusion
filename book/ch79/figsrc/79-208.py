import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ys = [12, 34, 56]
text(ax, 22, 74, r'sous-groupes $\supseteq\{0,4,8\}$', 'sujet', 's')
text(ax, 66, 74, 'sous-groupes du quotient', 'autre', 's')
for i in range(2):
    line(ax, [(22, ys[i] + 5), (22, ys[i + 1] - 5)], 'fixe')
    line(ax, [(66, ys[i] + 5), (66, ys[i + 1] - 5)], 'fixe')
for y, a, b in zip(ys, [3, 6, 12], [1, 2, 4]):
    box(ax, 7, y - 5, 30, 10, 'sujet', label='ordre %d' % a, size='s')
    box(ax, 51, y - 5, 30, 10, 'autre', label='ordre %d' % b, size='s')
    arrow(ax, (38, y), (50, y), 'varie')
text(ax, 44, 3, 'sous-groupe engendré : un sup', 'fixe', 's')
save(fig, '79-208')
