import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 72, r'$\mathbb{Z}$', 'sujet', 'xl')
text(ax, 66, 72, r'$F[x]$', 'autre', 'xl')
left = [r'$17=5\times3+2$', 'PGCD(12, 18) = 6', '7 est premier']
right = ['division avec reste', 'PGCD existe', 'irréductibles']
for i in range(3):
    y = 50 - 18 * i
    box(ax, 4, y, 38, 12, 'sujet', label=left[i], size='s')
    box(ax, 48, y, 36, 12, 'autre', label=right[i], size='s')
    arrow(ax, (42.5, y + 6), (47.5, y + 6), 'resultat', both=True)
text(ax, 44, 8, 'mêmes trois outils', 'resultat', 'm')
save(fig, '54-011')
