import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, 'chiffres : chapeaux reçus', 'fixe', 's')
groups = [(3, ['123'], 'gris', 'tous', '1 façon', 'fixe'), (19, ['132', '321', '213'], '', 'un seul', '3 façons', 'varie'), (59, ['231', '312'], '', 'personne', '2 façons', 'resultat')]
for x, cells, _, head, foot, role in groups:
    for i, c in enumerate(cells): box(ax, x + i * 12, 24, 11, 10, role, label=c, size='m')
    xa, xb = x, x + len(cells) * 12 - 1
    text(ax, (xa + xb) / 2, 40, head, role, 's')
    brace(ax, xa, xb, 24, role, label=foot, down=True)
save(fig, '80-371')
