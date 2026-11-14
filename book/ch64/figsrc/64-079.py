import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
labs = [r'$\mathbb{Z}$', r'$3\mathbb{Z}$', r'$6\mathbb{Z}$', r'$12\mathbb{Z}$']
ys = [62 - 14 * i for i in range(4)]
for i, y in enumerate(ys):
    x = 4 + 10 * i; w = 36 - 6 * i
    box(ax, x, y, w, 7, 'sujet', label=labs[i])
    nx = x + 14
    arrow(ax, (nx, y), (nx, (ys[i + 1] if i < 3 else 6) + 7), 'varie')
    if i < 3: text(ax, nx + 2, y - 3.5, 'insérer', 'varie', 's', ha='left')
box(ax, 34, 6, 12, 7, 'fixe', fill=False, dash=True, label=r'$\cdots$')
text(ax, 62, 9.5, r'jamais $\{0\}$', 'limite', 'm', ha='left', weight='bold')
save(fig, '64-079')
