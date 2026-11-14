import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for cx, k, v in ((20, 1, 2), (44, 2, 3), (68, 3, 5)):
    disc(ax, cx, 70, 6.5, 'sujet', label=r'$x_%d=%d$' % (k, v), size='s')
rows = [(52, r'$p_1$ : somme', r'$2+3+5=10$'),
        (36, r'$p_2$ : produits 2 à 2', r'$6+10+15=31$'),
        (20, r'$p_3$ : produit', r'$2\cdot3\cdot5=30$')]
for y, a, b in rows:
    box(ax, 3, y - 5, 34, 10, 'sujet', label=a, size='s')
    arrow(ax, (37, y), (43, y), 'varie')
    box(ax, 43, y - 5, 42, 10, 'resultat', label=b, size='m')
text(ax, 44, 6, "échanger les lettres ne change\nni " + r'$p_1$, ni $p_2$, ni $p_3$', 'fixe', 's')
save(fig, '65-101')
