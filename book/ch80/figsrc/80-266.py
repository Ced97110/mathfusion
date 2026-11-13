import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
box(ax, 2, 88, 84, 12, 'sujet', label='départ : ensemble ordonné fini $S$', size='s')
arrow(ax, (44, 88), (44, 80), 'fixe')
box(ax, 2, 44, 84, 36, 'varie', lw=1.6)
text(ax, 44, 74, 'étape décisive : ranger en liste', 'varie', 's', weight='bold')
text(ax, 44, 67, 'chaque nombre après ceux qui le divisent', 'encre', 's')
for i, d in enumerate([1, 2, 3, 4, 6, 12]):
    box(ax, 6 + 13.2 * i, 49, 11, 9, 'varie', label=str(d))
    if i < 5: arrow(ax, (17 + 13.2 * i, 53.5), (19.2 + 13.2 * i, 53.5), 'varie', 0.8)
arrow(ax, (44, 44), (44, 36), 'fixe')
box(ax, 2, 24, 84, 12, 'resultat', label='arrivée : $\\mu$ existe', size='s')
box(ax, 2, 4, 84, 14, 'limite', dash=True, label='6 avant 2 : l’équation de 6\ncontient plusieurs inconnues', size='s')
save(fig, '80-266')
