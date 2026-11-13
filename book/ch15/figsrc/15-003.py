import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 8, 49, 24, 7, 'sujet', label=r'$6n+40$'); box(ax, 40, 49, 24, 7, 'autre', label=r'$4n+70$')
s = 0.3
for lab, ya, yb, a, b, sg in (('n = 10', 38, 31, 100, 110, r'$<$'), ('n = 25', 21, 14, 190, 170, r'$>$')):
    text(ax, 8, (ya + yb) / 2 + 3 + 3, lab, 'encre', 's')
    box(ax, 17, ya, a * s, 6, 'sujet', label=f'{a} €', size='s')
    box(ax, 17, yb, b * s, 6, 'autre', label=f'{b} €', size='s')
    text(ax, 80, (ya + yb) / 2 + 3, sg, 'encre', 'xl', weight='bold')
arrow(ax, (8, 33), (8, 27), 'varie', both=True)
text(ax, 13, 30, '?', 'varie', 'l', weight='bold')
text(ax, 44, 4, "Où l'ordre change-t-il ?", 'varie', 'm', weight='bold')
save(fig, '15-003')
