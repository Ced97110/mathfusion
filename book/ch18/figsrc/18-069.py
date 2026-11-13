import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, 'produit 6 sur chaque ligne', 'sujet', 's')
rows = [(r'$1$ et $6$', r'$7$'), (r'$-1$ et $-6$', r'$-7$'), (r'$2$ et $3$', r'$5$'), (r'$-2$ et $-3$', r'$-5$')]
for k, (c, s) in enumerate(rows):
    y = 46 - 13 * k; good = (k == 2)
    box(ax, 8, y, 34, 10, 'resultat' if good else 'fixe', label=c)
    arrow(ax, (42, y + 5), (50, y + 5), 'resultat' if good else 'varie')
    box(ax, 50, y, 18, 10, 'resultat' if good else 'varie', label=s)
text(ax, 78, 46 - 26 + 5, 'produit 6,\nsomme 5 :\nla bonne', 'resultat', 's')
save(fig, '18-069')
