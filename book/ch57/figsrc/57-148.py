import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$c=x-2y$', 'varie', 'l', weight='bold')
rows = [(r'$(3\,;\,2)$', r'$3-2\times 2=-1$'), (r'$(1\,;\,1)$', r'$1-2\times 1=-1$'), (r'$(-1\,;\,0)$', r'$-1-2\times 0=-1$')]
ys = [44, 28, 12]
box(ax, 68, 8, 18, 50, 'resultat')
text(ax, 77, 36, r'$c=-1$', 'resultat', 's', weight='bold')
text(ax, 77, 29, 'même', 'resultat', 's')
text(ax, 77, 25, 'classe', 'resultat', 's')
for (c, k), y in zip(rows, ys):
    box(ax, 2, y, 21, 10, 'sujet', label=c)
    box(ax, 30, y, 32, 10, 'varie', label=k, size='s')
    arrow(ax, (23.5, y + 5), (29.5, y + 5), 'fixe', lw=0.9)
    arrow(ax, (62.5, y + 5), (67.5, y + 5), 'fixe', lw=0.9)
save(fig, '57-148')
