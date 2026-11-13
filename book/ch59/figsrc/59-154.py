import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 20, 58, 'division avec reste', 'fixe', 's')
box(ax, 2, 28, 36, 24, 'fixe', label='18 = 1 × 12 + 6\n12 = 2 × 6 + 0', size='s')
labs = ['chapitre 5\nPGCD = 6', 'chapitre 56\nanneaux euclidiens', 'chapitre 59\nforme normale']
for i, l in enumerate(labs):
    y = 52 - i * 19
    box(ax, 50, y, 36, 13, 'sujet', label=l, size='s')
    arrow(ax, (39, 40), (49, y + 6.5), 'varie')
save(fig, '59-154')
