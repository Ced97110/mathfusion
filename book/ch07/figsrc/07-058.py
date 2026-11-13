import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for x, a, b, r in ((28, '2', '3', 'sujet'), (60, '3', '5', 'autre')):
    text(ax, x, 49, a, r, 'xl'); text(ax, x, 33, b, r, 'xl')
    line(ax, [(x - 4, 41), (x + 4, 41)], r, lw=1.2)
arrow(ax, (31, 46), (57, 36), 'sujet', lw=1.2)
arrow(ax, (57, 46), (31, 36), 'autre', lw=1.2)
text(ax, 24, 19, r'$2\times5=10$', 'sujet', 'm'); text(ax, 64, 19, r'$3\times3=9$', 'autre', 'm')
text(ax, 44, 7, r'$10>9$, donc $\frac{2}{3}>\frac{3}{5}$', 'resultat', 'l')
text(ax, 44, 58, 'haut × bas, en croix', 'varie', 'm')
save(fig, '07-058')
