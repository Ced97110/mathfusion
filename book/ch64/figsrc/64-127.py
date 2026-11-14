import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
forms = ['un 3-cycle', 'un cycle long (≥ 4 objets)', 'deux 3-cycles', 'un 3-cycle et des échanges', 'seulement des échanges']
text(ax, 44, 76, r'$N\neq\{e\}$ : cinq formes possibles', 'encre', 's')
ys = [60 - 11 * k for k in range(5)]
for k, (y, f) in enumerate(zip(ys, forms)):
    box(ax, 2, y, 44, 9, 'sujet', label=f, size='s')
    arrow(ax, (46.5, y + 4.5), (58, 42.5 + (k - 2) * 4.5), 'varie')
box(ax, 58, 32, 28, 21, 'resultat', label='un élément de $N$\nqui bouge 3 objets :\nun 3-cycle', size='s')
box(ax, 2, ys[4], 44, 9, 'varie', fill=False, dash=True, lw=0.9)
text(ax, 24, 9, '5ᵉ objet utile ici seulement', 'varie', 's')
save(fig, '64-127')
