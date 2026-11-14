import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 80, 'une proportion est une équation', 'sujet', 's')
box(ax, 22, 62, 44, 14, 'sujet', label=r'$\frac{3}{5} = \frac{x}{20}$', size='l')
for cx, head, eq in [(23, r'× 20 des deux côtés', r'$x = 3 \times 20 \div 5$'), (65, 'produit en croix', r'$3 \times 20 = 5x$')]:
    arrow(ax, (33 if cx < 44 else 55, 62), (cx, 52), 'varie')
    text(ax, cx, 56 if False else 49, head, 'varie', 's')
    box(ax, cx - 20, 33, 40, 11, 'sujet', label=eq, size='m')
    arrow(ax, (cx + (6 if cx < 44 else -6), 33), (44, 19), 'resultat')
box(ax, 30, 6, 28, 12, 'resultat', label=r'$x$ = 12', size='l')
save(fig, '16-124')
