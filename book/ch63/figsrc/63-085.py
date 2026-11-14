import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 73, r'3 inconnues, 2 équations : $3>2$', 'fixe', 'm')
xs = [21, 41, 61]
for x, h in zip(xs, [r'$x_1$', r'$x_2$', r'$x_3$']):
    text(ax, x + 9.5, 64, h, 'varie', 'm')
coef = [['1', r'$\sqrt{2}$', r'$1+\sqrt{2}$'], ['1', r'$-\sqrt{2}$', r'$1-\sqrt{2}$']]
etas = [r'$\eta_1=1$', r'$\eta_2=\sigma$']
for i in range(2):
    y = 46 - 16 * i
    text(ax, 11, y + 6, etas[i], 'sujet', 's')
    for x, c in zip(xs, coef[i]):
        box(ax, x, y, 19, 12, 'sujet', label=c, size='s')
    text(ax, 84, y + 6, '= 0', 'varie', 's')
arrow(ax, (44, 29.5), (44, 13.5), 'resultat')
text(ax, 48, 21, 'donne', 'resultat', 's', ha='left')
box(ax, 18, 1, 68, 12, 'resultat', label=r'solution $(x_1,x_2,x_3)=(1,\ 1,\ -1)$', size='s')
save(fig, '63-085')
