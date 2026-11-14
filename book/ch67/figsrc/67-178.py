import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 12.5, 48, 'corps', 'fixe', 's')
text(ax, 37, 48, 'table', 'fixe', 's')
text(ax, 68.5, 48, 'produit', 'fixe', 's')
rows = [(30, 'autre', r'$\mathbb{F}_{16}$', '15 lignes', r'$a+b$, moins 15 si $>14$'),
        (10, 'sujet', r'$\mathbb{F}_{256}$', '255 lignes', r'$a+b$, moins 255 si $>254$')]
for y, role, corps, table, prod in rows:
    box(ax, 3, y, 19, 10, role, label=corps, size='s')
    arrow(ax, (22.2, y + 5), (27, y + 5), 'fixe')
    box(ax, 27, y, 20, 10, role, label=table)
    arrow(ax, (47.2, y + 5), (52, y + 5), 'fixe')
    box(ax, 52, y, 33, 10, role, label=prod, size='s')
text(ax, 12.5, 6, 'un octet', 'sujet', 's')
save(fig, '67-178')
