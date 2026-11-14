import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 16, 65, 'groupe', 'sujet', 's')
text(ax, 67, 65, 'corps', 'varie', 's')
ps = [2, 3, 2, 2]
for i, p in enumerate(ps):
    y = 50 - i * 13
    box(ax, 4, y, 24, 9, 'sujet', label=rf'$\mathbb{{Z}}/{p}$')
    box(ax, 48, y, 38, 9, 'varie', label=r'$\sqrt{a}$ : racine carrée' if p == 2 else r'$\sqrt[3]{a}$ : racine cubique', size='s')
    arrow(ax, (28, y + 4.5), (48, y + 4.5), 'fixe', both=True)
save(fig, '64-085')
