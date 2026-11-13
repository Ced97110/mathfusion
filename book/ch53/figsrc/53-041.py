import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
xs = [16, 44, 72]
top = [('A', 0), ('B', 1), ('C', 2)]
bot = [('D', 3), ('E', 4), ('F', 5)]
text(ax, 44, 79, 'clé 3 : tous avancent de 3', 'sujet', 'm', weight='bold')
for x, (l, n), (l2, n2) in zip(xs, top, bot):
    box(ax, x - 8, 56, 16, 9, 'fixe', label=f'{l} ({n})')
    box(ax, x - 8, 14, 16, 9, 'resultat', label=f'{l2} ({n2})')
    arrow(ax, (x, 56), (x, 24), 'varie', lw=1.2)
    text(ax, x + 5, 40, '+3', 'varie', 'm', weight='bold')
brace(ax, xs[0], xs[1], 67, 'fixe', label='1 cran', down=False)
brace(ax, xs[0], xs[1], 12, 'resultat', label='1 cran', down=True)
text(ax, 44, 3, 'l’écart ne change pas', 'resultat', 's')
save(fig, '53-041')
