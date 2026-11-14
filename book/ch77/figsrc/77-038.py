import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(44, [r'$\lambda^2$', r'$-T(a)\,\lambda$', r'$+N(a)$'], '$a$'),
        (28, [r'$\lambda^2$', r'$-4\lambda$', '$+5$'], '$2+i$'),
        (12, [r'$\lambda^2$', r'$-6\lambda$', '$+9$'], '$3$')]
RL = ['fixe', 'sujet', 'autre']
for y, labs, who in rows:
    text(ax, 9, y + 5, who, 'encre')
    for k in range(3):
        box(ax, 18 + 22 * k, y, 20, 10, RL[k], label=labs[k])
line(ax, [(2, 40), (84, 40)], 'fixe', 0.5, dash=True)
text(ax, 44, 58, '$n=2$ : forme fixe, nombres variables', 'fixe', 's')
save(fig, '77-038')
