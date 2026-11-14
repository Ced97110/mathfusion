import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for r in range(2):
    for c in range(2):
        hot = (r == 1 and c == 0)
        box(ax, 36.3 + 14 * c, 32.3 - 14 * r, 13.4, 13.4, 'varie' if hot else 'sujet',
            label=r'$a_{%d%d}$' % (r + 1, c + 1), size='l')
for c in range(2):
    text(ax, 43 + 14 * c, 50, f'colonne {c + 1}', 'varie' if c == 0 else 'fixe', 's')
for r in range(2):
    text(ax, 33, 39 - 14 * r, f'ligne {r + 1}', 'varie' if r == 1 else 'fixe', 's', ha='right')
text(ax, 78, 25, r'$i=2$, $j=1$', 'varie', 'm')
text(ax, 48, 10, r'$a_{ij}$ : ligne $i$, colonne $j$', 'sujet', 'm')
save(fig, '51-141')
