import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 44, 40, 42, 20, 'resultat')
text(ax, 65, 50, 'paquet de 0\n$=K$', 'resultat', 's', weight='bold')
box(ax, 44, 4, 42, 18, 'limite', label=r'paquet $\{1,\ 5,\ 9\}$', size='s')
for v, y in [('0', 56), ('4', 48), ('8', 40)]:
    disc(ax, 12, y, 3.6, 'resultat', label=v, size='s')
    arrow(ax, (16, y), (43.5, 50), 'resultat')
disc(ax, 12, 13, 3.6, 'limite', label='5', size='s')
arrow(ax, (16, 13), (43.5, 13), 'limite')
text(ax, 30, 25, r'$\nu$', 'varie', 'm')
text(ax, 44, 71, r'noyau de $\nu$ = $K$ = paquet de 0', 'sujet', 's', weight='bold')
text(ax, 12, 66, 'entiers', 'fixe', 's')
save(fig, '48-086')
