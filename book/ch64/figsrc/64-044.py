import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$S_n$ a $n!$ éléments', 'sujet', 'l', weight='bold')
text(ax, 8, 66, '3 choix', 'varie', 's')
text(ax, 52, 66, '2 choix ensuite', 'autre', 's')
files = [('1', ['1 2 3', '1 3 2']), ('2', ['2 1 3', '2 3 1']), ('3', ['3 1 2', '3 2 1'])]
for i, (d, fl) in enumerate(files):
    y = 54 - i * 14
    disc(ax, 8, y, 3.6, 'varie', label=d, size='m')
    arrow(ax, (12.4, y), (19.6, y), 'varie')
    box(ax, 20, y - 5, 64, 10, 'autre')
    text(ax, 38, y, fl[0], 'autre', 'm'); text(ax, 66, y, fl[1], 'autre', 'm')
text(ax, 44, 14, r'$3\times2\times1=6$ éléments', 'resultat', 'm', weight='bold')
text(ax, 44, 6, r'$n=4$ : $4\times3\times2\times1=24$', 'resultat', 'm')
save(fig, '64-044')
