import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [22, 36, 50, 64, 78]
for i, h in enumerate(['1 000', '100', '10', '1']):
    text(ax, (xs[i] + xs[i+1]) / 2, 62, h, 'fixe', 's')
box(ax, 22, 44, 14, 10, 'fixe', fill=False, dash=True)
for i, d in zip([1, 2, 3], '397'):
    box(ax, xs[i], 44, 14, 10, 'sujet', label=d, size='l')
for i, d in zip([0, 1, 2], '397'):
    box(ax, xs[i], 22, 14, 10, 'sujet', label=d, size='l')
box(ax, 64, 22, 14, 10, 'resultat', label='0', size='l', lw=1.2)
for i in [1, 2, 3]:
    c = (xs[i] + xs[i+1]) / 2
    arrow(ax, (c, 44), (c - 14, 32), 'varie')
text(ax, 12, 38, '× 10', 'varie', 'l')
text(ax, 44, 13, '397 × 100 = 39 700', 'resultat', 'm')
text(ax, 44, 6, 'deux cases à gauche', 'resultat', 's')
save(fig, '01-186')
