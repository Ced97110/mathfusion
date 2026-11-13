import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 3, 4, 82, 40, 'sujet', lw=1.0)
text(ax, 76, 37, r'$U$', 'sujet', 'l', weight='bold')
xs = [14 + i * 12 for i in range(6)]
box(ax, 8, 14, 40, 18, 'autre', fill=False, dash=True)
text(ax, 28, 36, r'$A$', 'autre', 'l')
for i, x in enumerate(xs):
    disc(ax, x, 23, 4.5, 'fixe' if i < 3 else 'sujet', label=str(i + 1))
text(ax, 62, 9, r'$x \in U$', 'varie', 'm')
arrow(ax, (62, 12), (62, 17.5), 'varie')
text(ax, 44, 52, r'$U$ = entiers de 1 à 6', 'sujet', 'l')
save(fig, '42-129')
