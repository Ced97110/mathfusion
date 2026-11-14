import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert math.gcd(5, 26) == 1 and math.gcd(2, 26) == 2 and (5 * 21) % 26 == 1

fig, ax = canvas(78)
box(ax, 26, 62, 36, 11, 'sujet', label=r'PGCD$(a, 26)$')
box(ax, 2, 42, 40, 10, 'resultat', label=r'PGCD $= 1$')
box(ax, 46, 42, 40, 10, 'limite', label=r'PGCD $> 1$')
arrow(ax, (36, 62), (22, 52.5), 'resultat')
arrow(ax, (52, 62), (66, 52.5), 'limite')
box(ax, 2, 24, 40, 10, 'resultat', fill=False, label=r'$a = 5$ : inverse 21', size='s')
box(ax, 46, 24, 40, 10, 'limite', fill=False, label=r'$a = 2$ : A et N, même image', size='s')
arrow(ax, (22, 42), (22, 34.5), 'resultat')
arrow(ax, (66, 42), (66, 34.5), 'limite')
box(ax, 2, 6, 40, 11, 'resultat', label='se déchiffre', weight='bold')
box(ax, 46, 6, 40, 11, 'limite', label='ne se déchiffre pas', weight='bold')
arrow(ax, (22, 24), (22, 17.5), 'resultat')
arrow(ax, (66, 24), (66, 17.5), 'limite')
save(fig, '53-056')
