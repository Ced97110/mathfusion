import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 22, 80, r'$\sigma_k$ : remplacements', 'sujet', 'm')
text(ax, 66, 80, 'restes modulo 5', 'autre', 'm')
ys = [68, 56, 44, 32]
for k, y in zip(range(1, 5), ys):
    box(ax, 8, y - 5, 28, 10, 'sujet', label=r'$\sigma_%d$' % k)
    box(ax, 54, y - 5, 24, 10, 'autre', label=str(k))
    arrow(ax, (37, y), (53, y), 'varie', both=True)
box(ax, 54, 15, 24, 10, 'fixe', fill=False, dash=True, label='0 : retiré', size='s')
box(ax, 4, 2, 40, 9, 'resultat', label=r'$\sigma_2$ après $\sigma_3$ = $\sigma_1$')
box(ax, 48, 2, 36, 9, 'resultat', label=r'$2 \times 3 = 6$, reste 1')
text(ax, 22, 19,'composer = multiplier', 'varie', 's')
save(fig, '63-163')
