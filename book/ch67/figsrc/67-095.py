import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
xs = [12, 44, 76]; y = 52
labs = [r'$\alpha+1$', r'$\alpha^2+1$', r'$\alpha^2+\alpha+1$']
for x, s in zip(xs, labs): box(ax, x - 10, y - 5, 20, 10, 'varie', label=s, size='s')
arrow(ax, (xs[0] + 11, y), (xs[1] - 11, y), 'fixe'); arrow(ax, (xs[1] + 11, y), (xs[2] - 11, y), 'fixe')
arrow(ax, (xs[2], y + 6), (xs[0], y + 6), 'fixe', curve=0.45)
text(ax, 27.5, y + 3.5, '1', 'fixe', 's'); text(ax, 60, y + 3.5, '2', 'fixe', 's'); text(ax, 44, y + 17, '3', 'fixe', 's')
calc = [r'1 : $(\alpha+1)^2=\alpha^2+2\alpha+1=\alpha^2+1$',
        r'2 : $(\alpha^2+1)^2=\alpha^4+1=\alpha^2+\alpha+1$',
        r'3 : $(\alpha^2+\alpha+1)^2=\alpha^4+\alpha^2+1=\alpha+1$']
for i, s in enumerate(calc): text(ax, 3, 30 - i * 10, s, 'varie', 's', ha='left')
text(ax, 3, 4, r'$2\alpha=0$ en caractéristique 2', 'fixe', 's', ha='left')
save(fig, '67-095')
