import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
order = lambda i, j: 1 if (i, j) == (0, 0) else (2 if i % 2 == 0 else 4)
role = {1: 'resultat', 2: 'fixe', 4: 'varie'}
text(ax, 30, 80, r'$\mathbb{Z}/4\oplus\mathbb{Z}/2$', 'sujet', 'm')
cw, ch = 17, 12
for i in range(4):
    for j in range(2):
        box(ax, 8 + j * (cw + 2), 62 - i * (ch + 2), cw, ch, role[order(i, j)], label=f'({i}, {j})')
for k, (o, lab) in enumerate([(1, 'ordre 1'), (2, 'ordre 2'), (4, 'ordre 4')]):
    box(ax, 52, 56 - k * 12, 8, 7, role[o], r=0.3)
    text(ax, 63, 59.5 - k * 12, lab, role[o], 's', ha='left')
text(ax, 66, 18, 'plus grand : 4', 'varie', 'm')
text(ax, 66, 11, 'jamais 8', 'limite', 'm')
save(fig, '60-101')
