import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 18, 64, r'premier 2 : $2^2$', 'sujet', 's')
text(ax, 47, 64, r'premier 3 : $3^1$', 'autre', 's')
rows = [(['2', '1'], r'$\mathbb{Z}/12$'), (['1 + 1', '1'], r'$\mathbb{Z}/2\oplus\mathbb{Z}/6$')]
for r, (opts, g) in enumerate(rows):
    y = 42 - r * 18
    box(ax, 4, y, 28, 10, 'sujet', label=opts[0])
    box(ax, 36, y, 22, 10, 'autre', label=opts[1])
    arrow(ax, (59, y + 5), (64, y + 5), 'varie')
    box(ax, 64, y, 22, 10, 'resultat', label=g, size='s')
text(ax, 44, 14, 'choix : 2 × 1 = 2 groupes', 'resultat', 'm')
save(fig, '60-107')
