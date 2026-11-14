import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# trois nombres voisins dans le plan : points, famille de 3 vecteurs, bases de 2 vecteurs
rows = [('points du plan', 'fixe', 'fixe', '∞', 0),
        ('famille\n(1, 0), (0, 1), (1, 1)', 'autre', 'autre', '3', 3),
        ('base\n(1, 0), (0, 1)', 'sujet', 'resultat', '2', 2),
        ('base\n(3, 1), (1, 2)', 'sujet', 'resultat', '2', 2)]
y = 58
for lab, r1, r2, cnt, k in rows:
    box(ax, 3, y, 46, 11, r1, label=lab, size='s')
    arrow(ax, (50, y + 5.5), (55, y + 5.5), 'fixe', lw=0.8)
    box(ax, 56, y + 1, 9, 9, r2, label=cnt, size='m', weight='bold')
    for i in range(k):
        box(ax, 68 + i * 6.4, y + 3, 5, 5, r1, r=0.3, lw=0.6)
    y -= 14
text(ax, 44, 6, r'$\dim V = 2$ : on compte les vecteurs d’une base', 'resultat', 's', weight='bold')
save(fig, '58-181')
