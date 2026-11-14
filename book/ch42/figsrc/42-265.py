import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(46, '(3, 4)', 'plus', '7', 'sujet', 'resultat', '2 entiers, 1 entier', 'resultat'),
        (26, '3', 'opposé', r'$-3$', 'limite', 'fixe', 'une seule entrée', 'limite'),
        (6, '(3, 4)', 'plus petit', 'oui', 'sujet', 'limite', 'sortie : oui ou non', 'limite')]
for y, a, op, b, ra, rb, v, rv in rows:
    box(ax, 2, y, 22, 10, ra, label=a); arrow(ax, (24, y + 5), (42, y + 5), 'varie'); text(ax, 33, y + 9, op, 'varie', 's')
    box(ax, 42, y, 16, 10, rb, label=b); box(ax, 60.5, y, 27, 10, rv, label=v, size='s')
save(fig, '42-265')
