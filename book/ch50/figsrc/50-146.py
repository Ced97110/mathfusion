import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 78, r'$60 = 5 \times 12$', 'sujet', 'l', weight='bold')
vals = [1, 2, 3, 4, 6, 12]
xs = [13 + i * 12.4 for i in range(6)]
text(ax, 44, 68, 'diviseurs de 12', 'fixe', 's')
for v, x in zip(vals, xs):
    box(ax, x - 5, 54, 10, 8, 'sujet' if v in (1, 6) else 'fixe', label=str(v))
x1, x6 = xs[0], xs[4]
text(ax, 38, 45, 'reste 1 modulo 5', 'varie', 's')
arrow(ax, (x1, 53.2), (x1, 36.8), 'varie'); arrow(ax, (x6, 53.2), (x6, 36.8), 'varie')
box(ax, x1 - 5, 28, 10, 8, 'sujet', label='1'); box(ax, x6 - 5, 28, 10, 8, 'sujet', label='6')
line(ax, [(x1 - 5, 28), (x1 + 5, 36)], 'limite', lw=1.4); line(ax, [(x1 - 5, 36), (x1 + 5, 28)], 'limite', lw=1.4)
text(ax, x1 + 2, 21, r'$A_5$ simple : pas 1', 'limite', 's', ha='left')
arrow(ax, (x6, 27.2), (x6, 13.8), 'resultat')
box(ax, x6 - 12, 5, 24, 8, 'resultat', label=r'$n_5 = 6$')
save(fig, '50-146')
