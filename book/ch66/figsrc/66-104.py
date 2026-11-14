import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 46, 12, 10, 'varie', label=r'$2^e$', size='m')
fc = [23 + 14 * i for i in range(5)]
for i, v in enumerate(['3', '5', '17', '257', '65 537']):
    box(ax, fc[i] - 6, 46, 12, 10, 'sujet', label=v, size='s')
ns = [(6, 'resultat'), (3, 'resultat'), (9, 'limite'), (15, 'resultat'), (17, 'resultat'), (7, 'limite')]
xs = [8.5 + 14 * i for i in range(6)]
for (n, r), x in zip(ns, xs):
    box(ax, x - 5.5, 12, 11, 10, r, label=str(n), size='m')
links = [(8.5, 8, 'resultat'), (8.5, fc[0] - 2, 'resultat'), (22.5, fc[0], 'resultat'),
         (34.5, fc[0] - 3, 'limite'), (38.5, fc[0] + 3, 'limite'),
         (50.5, fc[0] + 2, 'resultat'), (50.5, fc[1], 'resultat'), (64.5, fc[2], 'resultat')]
for x0, x1, r in links:
    line(ax, [(x0, 22.5), (x1, 45.5)], r, lw=1.0)
text(ax, 2, 6, r'vert : $2^e\times$ premiers distincts', 'resultat', 's', ha='left')
text(ax, 46, 6, 'rouge : répété ou absent', 'limite', 's', ha='left')
save(fig, '66-104')
