import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 4, 84, 50, 'fixe', fill=True)
text(ax, 44, 59, r'$S_3$ : les $3\times2\times1=6$ permutations', 'fixe', 's')
# six permutations : 3 colonnes, 2 rangées ; G_f en regroupe trois, dont l'identité
xs = [20, 44, 68]
for j, y in enumerate((38, 15)):
    for i, x in enumerate(xs):
        inside = (j == 0)
        disc(ax, x, y, 5, 'sujet' if inside else 'fixe', fill=True,
             label='1' if (i == 0 and j == 0) else None, size='m')
box(ax, 8, 28, 72, 20, 'sujet', fill=False, dash=True)
text(ax, 44, 51.2, r'$G_f$ : une partie de $S_3$, avec l’identité', 'sujet', 's')
text(ax, 44, 7.5, 'permutations hors de $G_f$', 'fixe', 's')
save(fig, '65-007')
