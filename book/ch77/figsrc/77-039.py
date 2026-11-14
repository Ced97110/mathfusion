import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
RL = ['fixe', 'sujet', 'autre']
for y, labs, tr, no in ((52, [r'$\lambda^2$', r'$-4\lambda$', '$+5$'], 4, 5), (20, [r'$\lambda^2$', r'$-6\lambda$', '$+9$'], 6, 9)):
    for k in range(3):
        box(ax, 4 + 26 * k, y, 24, 10, RL[k], label=labs[k])
    arrow(ax, (42, y), (42, y - 6), 'sujet'); arrow(ax, (68, y), (68, y - 6), 'autre')
    text(ax, 42, y - 10, f'trace {tr}', 'sujet'); text(ax, 68, y - 10, f'norme {no}', 'autre')
text(ax, 42, 70, 'début', 'sujet', 's'); text(ax, 68, 70, 'fin', 'autre', 's')
save(fig, '77-039')
