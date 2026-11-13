import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$I = k\mathbb{Z} = \{qk \mid q \in \mathbb{Z}\}$', 'sujet', 'l')
text(ax, 44, 66, r'avec $k = 5$', 'fixe', 's')
qs = [-2, -1, 0, 1, 2]
for i, q in enumerate(qs):
    x = 14 + i * 15
    box(ax, x - 6, 48, 12, 8, 'varie', label=str(q).replace('-', '−'), size='s')
    arrow(ax, (x, 48), (x, 39), 'fixe')
    box(ax, x - 6, 30, 12, 8, 'sujet', label=str(q * 5).replace('-', '−'), size='s')
    arrow(ax, (x, 30), (x, 20), 'resultat')
text(ax, 4, 60, r'$q$', 'varie', 's', ha='left')
text(ax, 4, 43.5, r'$\times\,5$', 'fixe', 's', ha='left')
text(ax, 4, 34, r'$qk$', 'sujet', 's', ha='left')
box(ax, 4, 6, 80, 12, 'resultat', label='… −10, −5, 0, 5, 10 … (tous)', size='s')
save(fig, '52-051')
