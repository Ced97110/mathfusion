import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
assert 2 * 4 + 3 * 1 == 11 and 2 * 0 + 3 * 1 == 3
# départ -> trois points de la preuve (la surjectivité porte le poids) -> arrivée, puis le cas chiffré
box(ax, 8, 74, 72, 10, 'fixe', label='départ : η fixée par les images de la base', size='s')
specs = [(2, 'injective :\nse lit sur les\nimages des sacs', 'sujet', 1.0, 'normal'),
         (31, 'surjective :\ncolonnes choisies\n(4, 0) et (1, 1) :\nη existe', 'varie', 2.4, 'bold'),
         (60, 'additive :\nse lit sur les\nimages des sacs', 'sujet', 1.0, 'normal')]
for x, lab, role, lw, wt in specs:
    box(ax, x, 42, 26, 24, role, label=lab, size='s', lw=lw, weight=wt)
    arrow(ax, (x + 13, 73.5), (x + 13, 66.5), 'fixe', lw=1.0)
    arrow(ax, (x + 13, 41.5), (x + 13, 34.5), 'varie' if role == 'varie' else 'fixe', lw=2.0 if role == 'varie' else 1.0)
text(ax, 47, 38, 'porte le poids', 'varie', 's', ha='left', weight='bold')
box(ax, 8, 23, 72, 11, 'resultat', label='arrivée : bijection compatible avec +', size='s')
text(ax, 44, 14, 'sacs : 2 de type 1 et 3 de type 2', 'encre', 's')
text(ax, 44, 7, r'$2(4,\,0)+3(1,\,1)=(11,\,3)$', 'encre', 's')
save(fig, '58-210')
